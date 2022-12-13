from rest_framework.serializers import ModelSerializer, SerializerMethodField

from speedpay_wallets.models import SpeedPayWallet


class SpeedPayWalletSerializer(ModelSerializer):
    """SpeedPay Wallet Model Serializer"""

    is_empty = SerializerMethodField()

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
