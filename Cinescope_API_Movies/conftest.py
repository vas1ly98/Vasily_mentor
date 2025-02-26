import pytest
import requests
from faker import Faker
from Cinescope_API_Movies.constants import MOVIES_GENRES_ENDPOINT, MOVIES_ENDPOINT, base_url
import pytest
from Cinescope_API_Movies.utils.data_generator import DataGenerator
from Cinescope_API_Movies.custom_requester.custom_requester import CustomRequester
from module_4.Reques_osnovi.requs import response

faker = Faker()
from Cinescope_API_Movies.api.api_manager import ApiManager
from  Cinescope_API_Movies.api.movies_api import MoviesAPI


@pytest.fixture(scope="function")
def temp_movie():
    return {'id': '1234',
            'name':'movie',
            'price':11,
            'description':'test',
            'imageUrl':'test',
            'location':'test',
            'published':True,
            'genreId': '7tyu',
            'rating':7,
            'createdAt':'10.10.2010'
            }

@pytest.fixture(scope="function")
def create_movie(api_manager, super_admin_token, movie_data):
    response = api_manager.movies_api.create_movie(movie_data, super_admin_token)
    movie_id = response.json()["id"]
    yield movie_id  # Возвращаем ID фильма
    # Удаляем фильм после теста
    api_manager.movies_api.delete_movie(movie_id, super_admin_token)


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