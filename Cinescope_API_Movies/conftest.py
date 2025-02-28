import pytest
import requests
from faker import Faker
from Cinescope_API_Movies.constants import MOVIES_GENRES_ENDPOINT, MOVIES_ENDPOINT, base_url, BASE_URL
import pytest
from Cinescope_API_Movies.utils.data_generator import DataGenerator
from Cinescope_API_Movies.custom_requester.custom_requester import CustomRequester
from constants import REGISTER_ENDPOINT, LOGIN_ENDPOINT
from random import randint
from Cinescope_API_Movies.api.api_manager import ApiManager
import time
faker = Faker()


#ФИКСТУРЫ ДЛЯ ФИЛЬМОВ
@pytest.fixture(scope="function")
def movie_data():
    random_movie = DataGenerator.generate_random_movie()
    random_description = DataGenerator.generate_random_description()
    return {
        "name": random_movie,
        "imageUrl": "https://example.com/movie.jpg",
        "price": randint(500, 1500),
        "description": random_description,
        "location": "MSK",
        "published": True,
        "genreId": randint(1, 9)

    }

@pytest.fixture(scope='function')
def temp_movie():
#тут создаем временный фильм, если значения не переданы будут использоваться из функции
    def create_movie_for_test(name='SUPERSONIC', imageUrl="https://example.com/movie.jpg", price=1000,
                              description="Описание тестового фильма", location="MSK", published=True, genreId=1):
        return {
            "name": name,
            "imageUrl": imageUrl,
            "price": price,
            "description": description,
            "location": location,
            "published": published,
            "genreId": genreId,
        }

    return create_movie_for_test


@pytest.fixture(scope="function")
def create_movie(api_manager, super_admin_token, movie_data):
    """Создает фильм и возвращает его данные, а после теста удаляет"""
    response = api_manager.movies_api.create_movie(movie_data, super_admin_token)
    movie = response.json()
    yield movie
    api_manager.movies_api.delete_movie(movie["id"], super_admin_token)
    time.sleep(2)




#ФИКСТУРЫ ДЛЯ СЕССИЙ
@pytest.fixture(scope="function")
def super_admin_token(api_manager):
    login_data = {
        "email": "test-admin@mail.com",  # Хардкодим данные супер-админа
        "password": "KcLMmxkJMjBD1",
    }
    response = api_manager.auth_api.login_user(login_data)
    return response.json()["accessToken"]


@pytest.fixture(scope="function")
def requester():
    """
    Фикстура для создания экземпляра CustomRequester.
    """
    session = requests.Session()
    return CustomRequester(session=session, base_url=BASE_URL)#

@pytest.fixture(scope="function")
def api_manager(session):
    """
    Фикстура для создания экземпляра ApiManager.
    """
    return ApiManager(session)

@pytest.fixture(scope="function")
def session():
    """
    Фикстура для создания HTTP-сессии.
    """
    http_session = requests.Session()
    yield http_session
    http_session.close()


# ФИКСТУРЫ ДЛЯ АУТЕНТЕФИКАЦИИ ПОЛЬЗОВАТЕЛЯ
@pytest.fixture(scope="function")
def test_user():
    """
    Генерация случайного пользователя для тестов.
    """
    random_email = DataGenerator.generate_random_email()
    random_name = DataGenerator.generate_random_name()
    random_password = DataGenerator.generate_random_password()

    return {
        "email": random_email,
        "fullName": random_name,
        "password": random_password,
        "passwordRepeat": random_password,
        "roles": ["USER"]
    }

@pytest.fixture(scope="function")
def registered_user(requester, test_user):
    """
    Фикстура для регистрации и получения данных зарегистрированного пользователя.
    """
    response = requester.send_request(
        method="POST",
        endpoint=REGISTER_ENDPOINT,
        data=test_user,
        expected_status=201
    )
    response_data = response.json()
    registered_user = test_user.copy()
    registered_user["id"] = response_data["id"]
    return registered_user



@pytest.fixture
def api_manager_with_auth(authorized_user, api_manager):
    """
    Возвращает API Manager с настроенным токеном авторизации.
    """
    api_manager.set_headers({"Authorization": f"Bearer {authorized_user['token']}"})
    return api_manager


