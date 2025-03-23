# from webbrowser import register
# import pytest
# import requests
# from faker import Faker
# from faker.generator import random
# from pycparser.ply.yacc import token
# from constants import HEADERS, BASE_URL, REGISTER_ENDPOINT, LOGIN_ENDPOINT
# from Cinescope.utils.data_generator import DataGenerator
# from Cinescope.custom_requester.custom_requester import CustomRequester
# from Cinescope.api.api_manager import ApiManager
# faker = Faker()
#
#
# @pytest.fixture(scope="function")
# def test_user():
#     """
#     Генерация случайного пользователя для тестов.
#
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
#
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
#
# @pytest.fixture(scope="function")
# def requester():
#     """
#     Фикстура для создания экземпляра CustomRequester.
#     """
#     session = requests.Session()
#     return CustomRequester(session=session, base_url=BASE_URL)
#
# @pytest.fixture(scope="function")
# def api_manager(session):
#     """
#     Фикстура для создания экземпляра ApiManager.
#     """
#     return ApiManager(session)
#
#
#
# @pytest.fixture(scope="function")
# def session():
#     """
#     Фикстура для создания HTTP-сессии.
#     """
#     http_session = requests.Session()
#     yield http_session
#     http_session.close()
#
#
# @pytest.fixture
# def api_manager_with_auth(authorized_user, api_manager):
#     """
#     Возвращает API Manager с настроенным токеном авторизации.
#     """
#     api_manager.set_headers({"Authorization": f"Bearer {authorized_user['token']}"})
#     return api_manager
