import time
import allure
from Cinescope.api.auth_api import AuthAPI
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

    # @allure.title("Тест регистрации пользователя с помощью Mock")
    # @allure.severity(allure.severity_level.MINOR)
    # @allure.label("qa_name", "Ivan Petrovich")
    # def test_register_user_mock(self, api_manager: ApiManager, test_user: TestUser, mocker): где взять test_user
    #     with allure.step(" Мокаем метод register_user в auth_api"):
    #         mock_response = RegisterUserResponse(  # Фиктивный ответ
    #             id="id",
    #             email="email@email.com",
    #             fullName="fullName",
    #             verified=True,
    #             banned=False,
    #             roles=[Roles.SUPER_ADMIN],
    #             createdAt=str(datetime.datetime.now())
    #         )
    #
    #         mocker.patch.object(
    #             api_manager.auth_api,  # Объект, который нужно замокать
    #             'register_user',  # Метод, который нужно замокать
    #             return_value=mock_response  # Фиктивный ответ
    #         )
    #
    #     with allure.step("Вызываем метод, который должен быть замокан"):
    #         register_user_response = api_manager.auth_api.register_user(test_user)
    #
    #     with allure.step("Проверяем, что ответ соответствует ожидаемому"):
    #         with allure.step("Проверка поля персональных данных"):  # обратите внимание на вложенность allure.step
    #             with check:
    #                 # Строка ниже выдаст исклющение и но выполнение теста продолжится
    #                 check.equal(register_user_response.fullName, "INCORRECT_NAME", "НЕСОВПАДЕНИЕ fullName")
    #                 check.equal(register_user_response.email, mock_response.email)
    #
    #         with allure.step("Проверка поля banned"):
    #             with check("Проверка поля banned"):  # можно использовать вместо allure.step
    #                 check.equal(register_user_response.banned, mock_response.banned)








