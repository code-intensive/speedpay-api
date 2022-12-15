from drf_spectacular import utils as schema_utils

users_serializer_schema = schema_utils.extend_schema_serializer(
    examples=[
        schema_utils.OpenApiExample(
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
        schema_utils.OpenApiExample(
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

users_viewset_schema = schema_utils.extend_schema_view(
    create=schema_utils.extend_schema(
        description=(
            "Registration endpoint for `SpeedPayUser`s.\n\n"
            "`first_name` and `last_name` fields are optional."
        ),
    ),
    list=schema_utils.extend_schema(
        description=(
            "Retrieves a paginated list of `SpeedPayUser`s.\n\n"
            "Default `offset` and `page_size` are 0 and 50 respectively."
        ),
    ),
    retrieve=schema_utils.extend_schema(
        description=(
            "Retrieves a `SpeedPayUser` via their `id`.\n\n"
            "Raises a **404** if the user does not exist."
        ),
    ),
    update=schema_utils.extend_schema(
        description=(
            "Updates a `SpeedPayUser` via their `id`.\n\n"
            "Raises a **404** if the user does not exist.\n\n"
        ),
        examples=[
            schema_utils.OpenApiExample(
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
    partial_update=schema_utils.extend_schema(
        description=(
            "Partially updates a `SpeedPayUser` via their `id`.\n\n"
            "Raises a **404** if the user does not exist.\n\n"
            "`username` and `email` fields are immutable."
        ),
        examples=[
            schema_utils.OpenApiExample(
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
    destroy=schema_utils.extend_schema(
        description=(
            "Deletes a `SpeedPayUser` via their `id`.\n\n"
            "Raises a **404** if the user does not exist.\n\n"
        ),
        responses={204: None},
    ),
)
