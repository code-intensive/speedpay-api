from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from speedpay_wallets.api.serializers import SpeedPayWalletSerializer
from speedpay_wallets.models import SpeedPayWallet
from utils.model_extractor import model_from_meta


class SpeedPayWalletViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = SpeedPayWalletSerializer

    @action(methods=("POST",), detail=False)
    def create_wallet(self, request) -> Response:
        """Creates a new wallet for the user"""
        if request.user.wallets.count() < 4:
            wallet = SpeedPayWallet.objects.create(speedpay_user=request.user)
            serialized_wallets = SpeedPayWalletSerializer(wallet).data
            return Response(serialized_wallets, status=status.HTTP_201_CREATED)
        return Response(
            "You have exceeded the max limit of wallets you can control",
            status=status.HTTP_400_BAD_REQUEST,
        )

    def get_queryset(self):
        wallets = model_from_meta(self.serializer_class)
        return wallets.objects.order_by()
