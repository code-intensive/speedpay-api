from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from speedpay_users.api.serializers import SpeedPayUserSerializer
from speedpay_users.models import SpeedPayUser


class SpeedPayUserViewSet(ModelViewSet):
    serializer_class = SpeedPayUserSerializer

    def get_queryset(self):
        return SpeedPayUser.objects.all()

    @action(methods=("GET",), detail=False)
    def me(self, request) -> Response:
        serialized_user_data = self.serializer_class(request.user).data
        return Response(serialized_user_data)
