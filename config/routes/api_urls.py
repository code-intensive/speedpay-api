from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from speedpay.users.api.views import SpeedPayUserViewSet
from speedpay.wallets.api.views import SpeedPayWalletViewSet

app_name = "api"

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", SpeedPayUserViewSet, basename="users")
router.register("wallets", SpeedPayWalletViewSet, basename="wallets")

urlpatterns = [
    path(f"{settings.BASE_API_ENDPOINT}/", include(router.urls)),
]
