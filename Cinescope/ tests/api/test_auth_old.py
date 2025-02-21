import pytest
import requests

from conftest import test_user # не будет работать если олд конфест
from constants_old import BASE_URL, HEADERS, REGISTER_ENDPOINT, LOGIN_ENDPOINT


class TestAuthAPI:
    def test_register_user(self, test_user):
        # URL для регистрации
        register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"

        # Отправка запроса на регистрацию
        response = requests.post(register_url, json=test_user, headers=HEADERS)

        print(f'Response status: {response.status_code}')
        print(f'Response body: {response.text}')

        assert response.status_code == 201, "Ошибка регистрации пользователя"
        response_data = response.json()
        assert response_data["email"] == test_user["email"], "Email не совпадает"

        assert "id" in response_data, "ID пользователя отсутствует в ответе"
        assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"

        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"


    def test_auth_user(self, test_user):

        login_url = f"{BASE_URL}{LOGIN_ENDPOINT}"
        login_data = {
            "email": test_user["email"],
            "password": test_user["password"]
        }
        response = requests.post(login_url, json = login_data, headers=HEADERS)
        assert response.status_code == 200, 'Ошибка авторизации'


        token = response.json().get("accessToken")
        assert token is not None, "Токен доступа отсутствует в ответе"

        user_email = response.json().get("user", {}).get("email")
        assert user_email is not None, "Ошибка: email отсутствует в ответе"

        refresh_token = response.json().get("refreshToken")
        if refresh_token:
            assert refresh_token is not None, "Рефреш токен отсутствует в ответе"
        else:
            print("Refresh token не возвращается в ответе, это нормально.")

        print(f"Response JSON: {response.json()}")

    def test_auth_user_negative_password(self, test_user):

        login_url = f"{BASE_URL}{LOGIN_ENDPOINT}"
        login_data = {
            "email": test_user["email"],
            "password": 'jora'
        }
        response = requests.post(login_url, json = login_data, headers=HEADERS)
        assert response.status_code == 401, 'Ошибка авторизации'

    def test_auth_user_negative_mail(self, test_user):

        login_url = f"{BASE_URL}{LOGIN_ENDPOINT}"
        login_data = {
            "email": 'jora@mail.ru',
            "password": test_user['password']
        }
        response = requests.post(login_url, json=login_data, headers=HEADERS)
        assert response.status_code == 401, 'Ошибка авторизации'

    def test_auth_user_negative_string(self, test_user):

        login_url = f"{BASE_URL}{LOGIN_ENDPOINT}"
        login_data = {
        }
        response = requests.post(login_url, json=login_data, headers=HEADERS)
        assert response.status_code == 401, 'Ошибка авторизации'



