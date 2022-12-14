from django.db.models import QuerySet
from django.http import HttpRequest
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from speedpay.users.api.serializers import SpeedPayUserSerializer
from speedpay.utils.model_extractor import model_from_meta


class SpeedPayUserViewSet(ModelViewSet):
    serializer_class = SpeedPayUserSerializer

    def get_queryset(self) -> QuerySet:
        speedpay_user = model_from_meta(self.serializer_class)
        # faster and prevents any sort of ordering
        return speedpay_user.objects.order_by()

    @action(methods=("GET",), detail=False)
    def me(self, request: HttpRequest) -> Response:
        """Returns details of the currently signed in User"""
        serialized_user = self.serializer_class(request.user).data
        return Response(serialized_user)