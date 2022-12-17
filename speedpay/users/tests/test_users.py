from typing import Any, Dict, Tuple

import pytest
from django.contrib.auth import get_user_model
from django.test.client import Client, RequestFactory
from rest_framework import status

SpeedPayUser = get_user_model()

pytestmark = pytest.mark.django_db


class TestWalletEndpoints:
    BASE_USERS_ENDPOINT = "/api/v1/users/"

    def test_create(
        self,
        client: Client,
        user_data: Dict[str, Any],
        rf: RequestFactory,
    ) -> None:
        request = rf.post(self.BASE_USERS_ENDPOINT)
        response = client.post(self.BASE_USERS_ENDPOINT, user_data)
        assert response.status_code == status.HTTP_201_CREATED
        assert SpeedPayUser.objects.count() == 1
        assert SpeedPayUser.objects.count() == 1
        assert (response.data["username"], response.data["email"]) == (
            user_data["username"],
            user_data["email"],
        )
        assert "id" in response.data
        assert "password" not in response.data

    def test_retrieve(
        self,
        user_and_client: Tuple[SpeedPayUser, Client],
        admin_client: Client,
    ) -> None:
        user, _ = user_and_client
        retrieve_endpoint = self.BASE_USERS_ENDPOINT + f"{user.id}/"
        response = admin_client.get(retrieve_endpoint)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["user_uuid"] == user.user_uuid
        assert response.data["email"] == user.email

    def test_list(self, admin_client: Client) -> None:
        response = admin_client.get(self.BASE_USERS_ENDPOINT)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) > 1

    # def test_patch(self, user_and_client: Tuple[SpeedPayUser, Client], admin_client:Client) -> None:
    #     user, _ = user_and_client
    #     update_endpoint = self.BASE_USERS_ENDPOINT + f"{user.id}/"
    #     new_data = json.dumps({"first_name": "changed", "last_name": "changed"})
    #     response = admin_client.patch(update_endpoint, new_data)
    #     assert response.status_code == status.HTTP_200_OK
    #     assert response.data["id"] == user.id
    #     assert response.data["first_name"] != user.first_name
    #     assert response.data["last_name"] == new_data["last_name"]

    def test_me(self, user_and_client: Tuple[SpeedPayUser, Client]) -> None:
        me_endpoint = self.BASE_USERS_ENDPOINT + "me/"
        speedpay_user, speedpay_client = user_and_client
        response = speedpay_client.get(me_endpoint)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["user_uuid"] == speedpay_user.user_uuid

    def test_user_does_not_exist(
        self,
        user_and_client: Tuple[SpeedPayUser, Client],
    ) -> None:
        user, speedpay_client = user_and_client
        retrieve_endpoint = self.BASE_USERS_ENDPOINT + "user_does_not_exist/"
        response = speedpay_client.get(retrieve_endpoint)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_retrieve_forbids_non_admin(
        self,
        user_and_client: Tuple[SpeedPayUser, Client],
    ) -> None:
        user, speedpay_client = user_and_client
        retrieve_endpoint = self.BASE_USERS_ENDPOINT + f"{user.id}/"
        response = speedpay_client.get(retrieve_endpoint)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_list_forbids_non_admin(
        self,
        user_and_client: Tuple[SpeedPayUser, Client],
    ) -> None:
        _, speedpay_client = user_and_client
        response = speedpay_client.get(self.BASE_USERS_ENDPOINT)
        assert response.status_code == status.HTTP_403_FORBIDDEN
