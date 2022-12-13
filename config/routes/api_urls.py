from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from speedpay_users.api.views import SpeedPayUserViewSet

app_name = "api"

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", SpeedPayUserViewSet, basename="speedpay_users")

urlpatterns = [
    path("api/", include(router.urls)),
]
