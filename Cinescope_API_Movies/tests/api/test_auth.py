from Cinescope_API_Movies.api.api_manager import  ApiManager
import time


import datetime
import pytest
import requests
from Cinescope_API_Movies.constants import BASE_URL, HEADERS, REGISTER_ENDPOINT,  LOGIN_ENDPOINT
from Cinescope_API_Movies.custom_requester.custom_requester import CustomRequester
from Cinescope_API_Movies.api.api_manager import  ApiManager
from Cinescope_API_Movies.enums.roles import Roles
from Cinescope_API_Movies.models.base_models import RegisterUserResponse, TestUser

class TestAuthAPI:
    def test_register_user(self, api_manager, test_user):
        """
        Тест на регистрацию пользователя.
        """
        response = api_manager.auth_api.register_user(test_user)
        response_data = response.json()

        # Проверки
        assert response_data["email"] == test_user["email"], "Email не совпадает"
        assert "id" in response_data, "ID пользователя отсутствует в ответе"
        assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"
        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"

    def test_register_and_login_user(self, api_manager: ApiManager, registered_user):
        """
        Тест на регистрацию и авторизацию пользователя.
        """
        login_data = {
            "email": registered_user["email"],
            "password": registered_user["password"]
        }
        response = api_manager.auth_api.login_user(login_data)
        response_data = response.json()

        # Проверки
        # assert "accessToken" in response_data, "Токен доступа отсутствует в ответе"
        # assert response_data["user"]["email"] == registered_user["email"], "Email не совпадает"

        register_user_response = RegisterUserResponse(**response.json())
        assert register_user_response.email == test_user.email, "Email не совпадает"

    def test_delete_user(self, api_manager: ApiManager, registered_user, super_admin_token):
        time.sleep(2)
        response = api_manager.auth_api.delete_user(
        registered_user["id"], super_admin_token, expected_status=404)  # Используем auth_api, если delete_user здесь
        assert response.status_code == 404, f"Ожидался статус 204, получен {response.status_code}"

