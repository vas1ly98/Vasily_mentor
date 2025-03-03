# @pytest.fixture(scope="function")
# def registered_user(requester, test_user):
#     """
#     Фикстура для регистрации и получения данных зарегистрированного пользователя.
#     """
#     response = requester.send_request(
#         method="POST",
#         endpoint=REGISTER_ENDPOINT,
#         data=test_user,
#         expected_status=201
#     )
#     response_data = response.json()
#     registered_user = test_user.copy()
#     registered_user["id"] = response_data["id"]
#     return registered_user

# @pytest.fixture(scope="function")
# def test_user():
#     """
#     Генерация случайного пользователя для тестов.
#     """
#     random_email = DataGenerator.generate_random_email()
#     random_name = DataGenerator.generate_random_name()
#     random_password = DataGenerator.generate_random_password()
#
#     return {
#         "email": random_email,
#         "fullName": random_name,
#         "password": random_password,
#         "passwordRepeat": random_password,
#         "roles": ["USER"]
#     }

#ФИКСТУРЫ ДЛЯ СЕССИЙ
# @pytest.fixture(scope="function")
# def super_admin_token(api_manager):
#     login_data = {
#         "email": "test-admin@mail.com",  # Хардкодим данные супер-админа
#         "password": "KcLMmxkJMjBD1",
#     }
#     response = api_manager.auth_api.login_user(login_data)
#     return response.json()["accessToken"]