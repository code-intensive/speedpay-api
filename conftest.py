from typing import Any, Dict, Tuple

import pytest
from django.contrib.auth import get_user_model
from django.test.client import Client

SpeedPayUser = get_user_model()


@pytest.fixture
def user_data() -> Dict[str, Any]:
    return {
        "username": "speedpay-user",
        "password": "9832iuebsd3289&$&@*ubsij",
        "first_name": "speedy",
        "last_name": "speedpay",
        "email": "speedpay@speedpay.ng",
    }


@pytest.fixture
def user_and_client(
    client: Client,
    user_data: Dict[str, Any],
) -> Tuple[SpeedPayUser, Client]:
    user = SpeedPayUser.objects.create(
        email=user_data["email"],
        username=user_data["username"],
        password=user_data["password"],
    )
    client.force_login(user)
    return user, client
