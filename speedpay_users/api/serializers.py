from rest_framework.serializers import ModelSerializer

from speedpay_users.models import SpeedPayUser


class SpeedPayUserSerializer(ModelSerializer):
    class Meta:
        model = SpeedPayUser
        fields = (
            "id",
            "password",
            "last_login",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_active",
            "uuid",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "uuid": {"read_only": True},
            "last_login": {"read_only": True},
            "id": {"read_only": True},
            "is_active": {"read_only": True},
        }
