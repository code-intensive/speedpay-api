from typing import Any, Dict

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from speedpay.users.api.schema import users_serializer_schema

SpeedPayUser = get_user_model()


@users_serializer_schema
class SpeedPayUserSerializer(serializers.ModelSerializer):
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
            "user_uuid",
        )
        extra_kwargs = {
            "user_uuid": {"read_only": True},
            "last_login": {"read_only": True},
            "id": {"read_only": True},
            "is_active": {"read_only": True},
            "password": {"write_only": True, "validators": [validate_password]},
        }

    def create(self, validated_data: Dict[str, Any]) -> SpeedPayUser:
        password = validated_data.pop("password")
        speedpay_user = SpeedPayUser(**validated_data)
        speedpay_user.set_password(password)
        speedpay_user.save()
        return speedpay_user
