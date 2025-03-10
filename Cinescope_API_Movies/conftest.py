from datetime import datetime

import pytest
import requests
import uuid
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Cinescope_API_Movies.constants import MOVIES_GENRES_ENDPOINT, MOVIES_ENDPOINT, base_url, BASE_URL
import pytest
from Cinescope_API_Movies.utils.data_generator import DataGenerator
from Cinescope_API_Movies.custom_requester.custom_requester import CustomRequester
from random import randint
from Cinescope_API_Movies.api.api_manager import ApiManager
from Cinescope_API_Movies.entities.user import User
from Cinescope_API_Movies.enums.roles import Roles
import time
faker = Faker()
from Cinescope_API_Movies.utils.user_data import UserData
from Cinescope_API_Movies.models.base_models import TestUser
from Cinescope_API_Movies.db_requester.models import UserDBModel


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

@pytest.fixture(scope="function")
def create_movie(api_manager, super_admin_token, movie_data):
    """Создает фильм и возвращает его данные, а после теста удаляет"""
    response = api_manager.movies_api.create_movie(movie_data, super_admin_token)
    movie = response.json()
    yield movie
    api_manager.movies_api.delete_movie(movie["id"], super_admin_token, expected_status=(201, 200, 404))
    time.sleep(2)

# @pytest.fixture
# def super_admin(api_manager):
#     """
#     Фикстура для создания супер-администратора.
#     """
#     admin_data = {
#         "email": "test-admin@mail.com",
#         "password": "KcLMmxkJMjBD1",
#         "passwordRepeat": "KcLMmxkJMjBD1"
#     }
#     login_response = api_manager.auth_api.login_user(admin_data)
#
#     assert login_response.status_code in [200, 201], "Не удалось авторизоваться"
#
#     access_token = login_response.json()["accessToken"]
#
#     yield access_token  # Возвращаем токен для авторизации в тестах по идее она же не нужна
#ФИКСТУРЫ ДЛЯ СЕССИЙ
@pytest.fixture(scope="function")
def super_admin_token(api_manager):
    """
    Фикстура для создания супер-администратора.
    """
    admin_data = {
        "email": "test-admin@mail.com",
        "password": "KcLMmxkJMjBD1",
        "passwordRepeat": "KcLMmxkJMjBD1"
    }
    login_response = api_manager.auth_api.login_user(admin_data)        # (admin_data.dict())
    assert login_response.status_code in [200, 201], "Не удалось авторизоваться"
    access_token = login_response.json()["accessToken"]
    yield access_token  # Возвращаем токен для авторизации в тестах


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
def test_user() -> TestUser: # добавили формат возвращаеммого значения TestUser
    """
    Генерация случайного пользователя для тестов.
    """
    random_email = DataGenerator.generate_random_email()
    random_name = DataGenerator.generate_random_name()
    random_password = DataGenerator.generate_random_password()

    return TestUser( # возвращем обьект с опередленный набором полей и правил. нет возможности добавить чтото еще
        email=random_email,
        fullName=random_name,
        password=random_password,
        passwordRepeat=random_password, # field_validator автоматически проверит, что password и passwordRepeat совпадают
    ) # поле roles заполнится автоматически и бедт = [Role.USER]


@pytest.fixture(scope="function")
def registered_user(api_manager, test_user: TestUser):
    """
    Фикстура для регистрации пользователя через auth_api.
    """
    response = api_manager.auth_api.register_user(test_user)
    response_data = response.json()
    test_user.id = response_data["id"]
    return test_user



@pytest.fixture(scope="function")
def user_create(api_manager, super_admin_token):
    """Фикстура для создания пользователей с разными ролями."""
    created_users = []

    def _user_create(role):
        # ✅ Генерируем данные пользователя
        user_data = UserData.generate_user_data(role)
        email, password = user_data.email, user_data.password

        # ✅ Регистрируем пользователя
        response = api_manager.auth_api.register_user(user_data)

        if response.status_code == 201:
            user_id = response.json().get("id") or response.json().get("user", {}).get("id")
        elif response.status_code == 409:  # Пользователь уже существует
            login_response = api_manager.auth_api.login_user({"email": email, "password": password})
            assert login_response.status_code in [200, 201], "❌ Ошибка: не удалось авторизоваться"
            user_id = login_response.json()["user"]["id"]
        else:
            raise ValueError(f"❌ Ошибка: неожиданный статус {response.status_code} при регистрации")

        # ✅ Логинимся один раз, чтобы получить токен
        access_token = login_response.json()["accessToken"] if response.status_code == 409 else \
                       api_manager.auth_api.login_user({"email": email, "password": password}).json()["accessToken"]

        # ✅ Если роль не USER, обновляем через супер-админа
        if role != "USER":
            api_manager.auth_api.change_user_role(user_id, [role], super_admin_token)

        created_users.append(user_id)  # ✅ Добавляем пользователя в список

        return {"id": user_id, "email": email,"password": user_data.password, "token": access_token}

    yield _user_create

    # ✅ Удаляем пользователей после тестов
    for user_id in created_users:
        try:
            api_manager.auth_api.delete_user(user_id, super_admin_token)
        except Exception as e:
            print(f"⚠️ Ошибка при удалении пользователя {user_id}: {e}")


@pytest.fixture(scope="function")
def db_session():
    # Оставим эти данные тут для наглядности. но не стоит хранить креды в гитлбе. они должны быть заданы через env
    HOST = "92.255.111.76"
    PORT = 31200
    DATABASE_NAME = "db_movies"
    USERNAME = "postgres"
    PASSWORD = "AmwFrtnR2"

    engine = create_engine(
        f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}")  # Создаем движок (engine) для подключения к базе данных
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # Создаем фабрику сессий
    """
    Фикстура, которая создает и возвращает сессию для работы с базой данных.
    После завершения теста сессия автоматически закрывается.
    """
    # Создаем новую сессию
    session = SessionLocal()
    test_user = UserDBModel(
        id="test_id",
        email=DataGenerator.generate_random_email(),
        full_name=DataGenerator.generate_random_name(),
        password=DataGenerator.generate_random_password(),
        created_at=datetime.now(),
        updated_at=datetime.now(),
        verified=False,
        banned=False,
        roles="{USER}"
    )
    session.add(test_user)  # добавляем обьект в базу данных
    session.commit()  # сохраняем изменения для всех остальных подключений

    yield session  # можете запустить тесты в дебаг режиме и поставить тут брекпойнт
    # зайдите в базу и убедитесь что нывй обьект был создан

    # код ниже выполнится после всех запущеных тестов
    session.delete(test_user)  # Удаляем тестовые данные
    session.commit()  # сохраняем изменения для всех остальных подключений
    session.close()  # завершем сессию (отключаемся от базы данных)













# @pytest.fixture
# def movie_data():
#     """
#     Генерация данных для создания фильма.
#     """
#     return {
#         "name": "Test Movie",
#         "price": 500,
#         "description": "Описание тестового фильма",
#         "location": "MSK",  # Исправлено значение location
#         "published": True,
#         "genreId": 1  # Исправлено значение genreId
#     }


# @pytest.fixture
# def api_manager_with_auth(authorized_user, api_manager):
#     """
#     Возвращает API Manager с настроенным токеном авторизации.
#     """
#     api_manager.set_headers({"Authorization": f"Bearer {authorized_user['token']}"})
#     return api_manager


