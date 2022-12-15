from drf_spectacular import utils as schema_utils

wallet_serializer_schema = schema_utils.extend_schema_serializer(
    examples=[
        schema_utils.OpenApiExample(
            "wallets",
            value={
                "id": 1938,
                "wallet_uuid": "wallet_88d00e8f927f449291a1654b3f7cb298",
                "balance": "198279.00",
                "is_active": True,
                "last_withdrawn": "2022-12-14T23:13:49.438Z",
                "last_deposited": "2022-12-14T23:13:49.438Z",
                "is_empty": False,
            },
        ),
    ],
)

wallet_viewset_schema = schema_utils.extend_schema_view(
    create=schema_utils.extend_schema(
        request=None,
    ),
    list=schema_utils.extend_schema(
        description=(
            "Retrieves a paginated list of `SpeedPayWallet`s.\n\n"
            "Default `offset` and `page_size` are 0 and 50 respectively."
        ),
        examples=[
            schema_utils.OpenApiExample(
                "speedpay_wallets_patch_request",
                value=[
                    {
                        "id": 1938,
                        "wallet_uuid": "wallet_88d00e8f927f449291a1654b3f7cb298",
                        "balance": "178279.00",
                        "is_active": True,
                        "last_withdrawn": "2022-10-14T20:13:31.408Z",
                        "last_deposited": "2022-12-14T23:21:43.438Z",
                        "is_empty": False,
                    },
                    {
                        "id": 1939,
                        "wallet_uuid": "wallet_88d00e8f927f449291a1654b3f7cb298",
                        "balance": "0.00",
                        "is_active": True,
                        "last_withdrawn": "2022-12-14T23:13:49.411Z",
                        "last_deposited": "2022-08-14T03:09:49.439Z",
                        "is_empty": True,
                    },
                ],
                response_only=True,
            ),
        ],
    ),
    retrieve=schema_utils.extend_schema(
        description=(
            "Retrieves a `SpeedPayWallet` via their `wallet_uuid`.\n\n"
            "Raises a **404** if the wallet does not exist."
        ),
    ),
    update=schema_utils.extend_schema(
        description=(
            "Updates a `SpeedPayWallet` via their `wallet_uuid`.\n\n"
            "Raises a **404** if the wallet does not exist.\n\n"
        ),
        examples=[
            schema_utils.OpenApiExample(
                "speedpay_wallets_update_request",
                value={
                    "id": 1939,
                    "wallet_uuid": "wallet_88d00e8f927f449291a1654b3f7cb298",
                    "balance": "0.00",
                    "is_active": True,
                    "last_withdrawn": "2022-12-14T23:13:49.411Z",
                    "last_deposited": "2022-08-14T03:09:49.439Z",
                    "is_empty": True,
                },
                request_only=True,
            ),
        ],
    ),
    partial_update=schema_utils.extend_schema(
        description=(
            "Partially updates a `SpeedPayWallet` via their `wallet_uuid`.\n\n"
            "Raises a **404** if the wallet does not exist.\n\n"
            "Only the `is_active` field can be mutated."
        ),
        examples=[
            schema_utils.OpenApiExample(
                "speedpay_wallets_patch_request",
                value={
                    "is_active": False,
                },
                request_only=True,
            ),
        ],
    ),
    destroy=schema_utils.extend_schema(
        description=(
            "Deletes a `SpeedPayWallet` via it's `wallet_uuid`.\n\n"
            "Raises a **404** if the wallet does not exist.\n\n"
        ),
        responses={204: None},
    ),
    me=schema_utils.extend_schema(
        examples=[
            schema_utils.OpenApiExample(
                "speedpay_wallets_patch_request",
                value=[
                    {
                        "id": 1938,
                        "wallet_uuid": "wallet_88d00e8f927f449291a1654b3f7cb298",
                        "balance": "178279.00",
                        "is_active": True,
                        "last_withdrawn": "2022-10-14T20:13:31.408Z",
                        "last_deposited": "2022-12-14T23:21:43.438Z",
                        "is_empty": False,
                    },
                    {
                        "id": 1939,
                        "wallet_uuid": "wallet_88d00e8f927f449291a1654b3f7cb298",
                        "balance": "0.00",
                        "is_active": True,
                        "last_withdrawn": "2022-12-14T23:13:49.411Z",
                        "last_deposited": "2022-08-14T03:09:49.439Z",
                        "is_empty": True,
                    },
                ],
                response_only=True,
            ),
        ],
    ),
)
