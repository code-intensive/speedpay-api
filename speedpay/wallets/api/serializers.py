from typing import Any, Dict

from rest_framework import serializers

from speedpay.wallets.api.schema import wallet_serializer_schema
from speedpay.wallets.models import SpeedPayWallet


@wallet_serializer_schema
class SpeedPayWalletSerializer(serializers.ModelSerializer):
    """SpeedPay Wallet Model Serializer"""

    is_empty = serializers.SerializerMethodField()
    _links = serializers.SerializerMethodField(method_name="links")

    class Meta:
        model = SpeedPayWallet
        fields = (
            "id",
            "wallet_uuid",
            "balance",
            "is_active",
            "last_withdrawn",
            "last_deposited",
            "is_empty",
            "_links",
        )
        read_only_fields = (
            "id",
            "wallet_uuid",
            "balance",
            "is_active",
            "last_withdrawn",
            "last_deposited",
            "is_empty",
        )

    def get_is_empty(self, wallet: SpeedPayWallet) -> bool:
        """Dynamic field for creating is_empty data for serializer response"""
        return wallet.is_empty

    def links(self, wallet: SpeedPayWallet) -> Dict[str, Any]:

        return {
            "self": {
                "href": f"http://127.0.0.1:8000/api/v1/wallets/{wallet.wallet_uuid}/",
            },
            "collection": {"href": f"http://127.0.0.1:8000/api/v1/wallets"},
            "deposit": {
                "href": f"http://127.0.0.1:8000/api/v1/wallets/{wallet.wallet_uuid}/deposit",
            },
            "withdraw": {
                "href": f"http://127.0.0.1:8000/api/v1/wallets/{wallet.wallet_uuid}/withdraw/",
            },
            "balance": {
                "href": f"http://127.0.0.1:8000/api/v1/wallets/{wallet.wallet_uuid}/check-balance/",
            },
        }
