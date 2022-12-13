from django.db.models import QuerySet
from rest_framework.viewsets import ModelViewSet

from speedpay_wallet.api.serializers import SpeedPayWalletSerializer
from utils.model_extractor import model_from_meta


class SpeedPayWalletViewSet(ModelViewSet):
    """Wallet API viewset"""

    serializer_class = SpeedPayWalletSerializer

    def get_queryset(self) -> QuerySet:
        wallet = model_from_meta(self.serializer_class)
        # faster and prevents any sort of ordering
        return wallet.objects.order_by()
