from rest_framework.serializers import ModelSerializer, SerializerMethodField

from speedpay_wallet.models import SpeedPayWallet


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
        extra_kwargs = {
            "id": {"read_only": True},
            "wallet_uuid": {"read_only": True},
            "balance": {"read_only": True},
            "last_withdraw": {"read_only": True},
            "last_deposited": {"read_only": True},
            "is_empty": {"read_only": True},
        }

    def get_is_empty(self, wallet: SpeedPayWallet) -> bool:
        """Dynamic field for creating is_empty data for serializer response"""
        return wallet.is_empty
