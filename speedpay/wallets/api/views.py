from typing import Dict, Union

from django.db.models import QuerySet
from django.http import HttpRequest
from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from speedpay.authentication.permissions import IsAdminUserOrNoList
from speedpay.core.pagination import SpeedPayWalletPaginator
from speedpay.utils.model_extractor import model_from_meta
from speedpay.wallets.api.serializers import SpeedPayWalletSerializer


@extend_schema(
    examples=[
        OpenApiExample(
            "wallets",
            value={
                "id": 1938,
                "wallet_uuid": "wallet_88d00e8f927f449291a1654b3f7cb298",
                "balance": "198279",
                "is_active": True,
                "last_withdrawn": "2022-12-14T23:13:49.438Z",
                "last_deposited": "2022-12-14T23:13:49.438Z",
                "is_empty": False,
            },
        ),
    ],
)
class SpeedPayWalletViewSet(ListModelMixin, GenericViewSet):
    serializer_class = SpeedPayWalletSerializer
    lookup_field = "wallet_uuid"
    lookup_url_kwarg = "wallet_uuid"
    permission_classes = (IsAdminUserOrNoList,)
    pagination_class = SpeedPayWalletPaginator

    @extend_schema(
        request=None,
        responses={201: SpeedPayWalletSerializer},
    )
    def create(self, request: HttpRequest, *args, **kwargs) -> Response:
        """Creates a new wallet for the user"""
        wallet_model = model_from_meta(self.serializer_class)
        wallet = wallet_model.objects.create(speedpay_user=request.user)
        serialized_wallet = self.get_serializer(wallet).data
        return Response(serialized_wallet, status=status.HTTP_201_CREATED)

    @action(methods=("GET",), detail=False)
    def me(self, request: HttpRequest) -> Response:
        """Returns wallets owned by the currently signed in User"""
        wallets = request.user.wallets.order_by()
        serialized_wallets = self.get_serializer(wallets, many=True).data
        return Response(serialized_wallets)

    @action(methods=("POST",), detail=True)
    def withdraw(self, request: HttpRequest, *args, **kwargs) -> Response:
        """Makes a withdrawal from the authenticated User's wallet"""
        amount = SpeedPayWalletViewSet._get_amount_or_fail(request.data)
        wallet = self.get_object()
        wallet.withdraw(amount)
        serialized_wallet = self.get_serializer(wallet).data
        return Response(serialized_wallet)

    @action(methods=("POST",), detail=True)
    def deposit(self, request: HttpRequest, *args, **kwargs) -> Response:
        """Makes a deposit to the authenticated User's wallet"""
        amount = SpeedPayWalletViewSet._get_amount_or_fail(request.data)
        wallet = self.get_object()
        wallet.deposit(amount)
        serialized_wallet = self.get_serializer(wallet).data
        return Response(serialized_wallet)

    @action(methods=("GET",), detail=True, url_path="check-balance")
    def check_balance(self, request: HttpRequest, *args, **kwargs) -> Response:
        """Checks the current balance in the authenticated User's wallet"""
        wallet = self.get_object()
        return Response({"balance": wallet.balance})

    def get_queryset(self) -> QuerySet:
        wallets = model_from_meta(self.serializer_class)
        return wallets.objects.order_by()

    def _get_amount_or_fail(data: Dict[str, Union[str, int]]) -> Union[int, str]:
        """
        Attempts to retrieve the amount from the provided data,
        :raises: `ValidationError` in the event of failure
        """
        amount = data.get("amount", None)
        if amount is None:
            raise ValidationError(
                detail={"amount": ["Missing required field."]},
            )
        if amount < 1:
            raise ValidationError(
                detail={"amount": ["Amount must exceed zero."]},
                code="invalid_amount",
            )
        return amount
