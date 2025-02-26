from constants import REGISTER_ENDPOINT, LOGIN_ENDPOINT
import pytest
import requests
from Cinescope.constants import BASE_URL, HEADERS, REGISTER_ENDPOINT,  LOGIN_ENDPOINT
from Cinescope.custom_requester.custom_requester import CustomRequester
from Cinescope.api.api_manager import  ApiManager
import time




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
        assert "accessToken" in response_data, "Токен доступа отсутствует в ответе"
        assert response_data["user"]["email"] == registered_user["email"], "Email не совпадает"


    # def test_delete_user(self, api_manager: ApiManager, registered_user):
    #     time.sleep(2)
    #     response = api_manager.auth_api.delete_user(
    #         registered_user["id"], expected_status=400)  # Используем auth_api, если delete_user здесь
    #     assert response.status_code == 400, f"Ожидался статус 204, получен {response.status_code}"


