import pytest
import requests
from faker import Faker
from Cinescope_API_Movies.constants import MOVIES_GENRES_ENDPOINT, MOVIES_ENDPOINT, base_url
import pytest
from Cinescope_API_Movies.utils.data_generator import DataGenerator
from Cinescope_API_Movies.custom_requester.custom_requester import CustomRequester
from constants import REGISTER_ENDPOINT, LOGIN_ENDPOINT
from random import randint
faker = Faker()
from Cinescope_API_Movies.api.api_manager import ApiManager


#ФИКСТУРЫ ДЛЯ ФИЛЬМОВ
@pytest.fixture(scope="function")
def movie_data():
    return {
        "name": f"movie{randint(1, 1000)}",#по идее тут тоже надо генератор сделать будет да, чтобы рандомные имена были то если повторно то 409 ошибка
        "imageUrl": "https://example.com/movie.jpg",
        "price": 500,
        "description": "Описание тестового фильма",
        "location": "MSK",
        "published": True,
        "genreId": 1,

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
    response = api_manager.movies_api.create_movie(movie_data, super_admin_token)
    movie_id = response.json()["id"]
    yield movie_id  # Возвращаем ID фильма
    # Удаляем фильм после теста
    api_manager.movies_api.delete_movie(movie_id, super_admin_token)




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
    return CustomRequester(session=session, base_url=base_url)

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


