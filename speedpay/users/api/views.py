from django.db.models import QuerySet
from django.http import HttpRequest
from drf_spectacular import utils as spectacular_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from speedpay.authentication.permissions import IsAuthenticatedOrAnonCreate
from speedpay.core.pagination import SpeedPayUserPaginator
from speedpay.users.api.serializers import SpeedPayUserSerializer
from speedpay.utils.model_extractor import model_from_meta


@spectacular_schema.extend_schema_view(
    create=spectacular_schema.extend_schema(
        description=(
            "Registration endpoint for `SpeedPayUser`s.\n\n"
            "`first_name` and `last_name` fields are optional."
        ),
    ),
    list=spectacular_schema.extend_schema(
        description=(
            "Retrieves a paginated list of `SpeedPayUser`s.\n\n"
            "Default `offset` and `page_size` are 0 and 50 respectively."
        ),
    ),
    retrieve=spectacular_schema.extend_schema(
        description=(
            "Retrieves a `SpeedPayUser` via their `id`.\n\n"
            "Raises a **404** if the user does not exist."
        ),
    ),
    update=spectacular_schema.extend_schema(
        description=(
            "Updates a `SpeedPayUser` via their `id`.\n\n"
            "Raises a **404** if the user does not exist.\n\n"
        ),
        examples=[
            spectacular_schema.OpenApiExample(
                "speedpay_users_patch_request",
                value={
                    "first_name": "elon",
                    "last_name": "musk",
                    "password": "*Ujki87UUidjhvjs)I",
                },
                request_only=True,
            ),
        ],
    ),
    partial_update=spectacular_schema.extend_schema(
        description=(
            "Partially updates a `SpeedPayUser` via their `id`.\n\n"
            "Raises a **404** if the user does not exist.\n\n"
            "`username` and `email` fields are immutable."
        ),
        examples=[
            spectacular_schema.OpenApiExample(
                "speedpay_users_patch_request",
                value={
                    "first_name": "elon",
                    "last_name": "musk",
                    "password": "*Ujki87UUidjhvjs)I",
                },
                request_only=True,
            ),
        ],
    ),
    destroy=spectacular_schema.extend_schema(
        description=(
            "Deletes a `SpeedPayUser` via their `id`.\n\n"
            "Raises a **404** if the user does not exist.\n\n"
        ),
        responses={204: None},
    ),
)
@spectacular_schema.extend_schema(
    examples=[
        spectacular_schema.OpenApiExample(
            "speedpay_users_create_request",
            value={
                "username": "elon",
                "first_name": "elon",
                "last_name": "musk",
                "email": "elon@tesla.com",
                "password": "*Ujki87UUidjhvjs)I",
            },
            request_only=True,
        ),
        spectacular_schema.OpenApiExample(
            "speedpay_users_response",
            value={
                "id": 19478,
                "last_login": "2022-12-15T00:22:09.805Z",
                "username": "elon",
                "first_name": "elon",
                "last_name": "musk",
                "email": "elon@tesla.com",
                "is_active": True,
                "user_uuid": "user_88d00e8f927f4492bnma1654b3f7cb298",
            },
            response_only=True,
        ),
    ],
)
class SpeedPayUserViewSet(ModelViewSet):
    serializer_class = SpeedPayUserSerializer
    permission_classes = (IsAuthenticatedOrAnonCreate,)
    pagination_class = SpeedPayUserPaginator

    def get_queryset(self) -> QuerySet:
        speedpay_user = model_from_meta(self.serializer_class)
        # faster and prevents any sort of ordering
        return speedpay_user.objects.order_by()

    @action(methods=("GET",), detail=False)
    def me(self, request: HttpRequest) -> Response:
        """Returns details of the currently signed in `SpeedPayUser`"""
        serialized_user = self.serializer_class(request.user).data
        return Response(serialized_user)
