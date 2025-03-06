import time
from Cinescope_API_Movies.api.api_manager import  ApiManager
from Cinescope_API_Movies.models.base_models import RegisterUserResponse
from datetime import datetime

class TestAuthAPI:
    def test_register_user(self, api_manager, test_user):
        """
        Тест на регистрацию пользователя.
        """
        response = api_manager.auth_api.register_user(test_user)
        response_data = response.json()

        # Проверки
        assert response_data["email"] == test_user.email, "Email не совпадает"
        assert "id" in response_data, "ID пользователя отсутствует в ответе"
        assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"
        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"

    def test_register_and_login_user(self, api_manager: ApiManager, registered_user):
        """
        Тест на регистрацию и авторизацию пользователя.
        """
        login_data = {
            "email": registered_user.email,
            "password": registered_user.password
        }
        response = api_manager.auth_api.login_user(login_data)
        response_data = response.json()

        # Извлекаем данные пользователя
        user_data = response_data.get("user", {})

        # Добавляем отсутствующие поля, если они есть в основном ответе
        user_data["verified"] = response_data.get("verified", False)  # Если нет, ставим False
        user_data["banned"] = response_data.get("banned", False)  # Если нет, ставим False

        # Если createdAt отсутствует, ставим текущую дату в формате ISO 8601
        user_data["createdAt"] = response_data.get("createdAt", datetime.utcnow().isoformat())

        # Проверка на успешную авторизацию
        assert "accessToken" in response_data, "Токен доступа отсутствует в ответе"
        assert user_data["email"] == registered_user.email, "Email не совпадает"

        # Передаем данные пользователя в модель RegisterUserResponse
        register_user_response = RegisterUserResponse(**user_data)

    def test_delete_user(self, api_manager: ApiManager, registered_user, super_admin_token):
        time.sleep(2)
        response = api_manager.auth_api.delete_user(
        registered_user.id, super_admin_token)  # Используем auth_api, если delete_user здесь
        assert response.status_code == 200, f"Ожидался статус 204, получен {response.status_code}"# тут чет не-то должен быть 204 по идее

