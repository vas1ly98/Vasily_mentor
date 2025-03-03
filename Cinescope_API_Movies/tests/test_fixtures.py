from Cinescope_API_Movies.conftest import api_manager, create_movie, super_admin_token


class TestFixtures:
    def test_auth_token(self, super_admin_token):

        assert super_admin_token is not None, "Токен авторизации должен быть не пустым"
        assert super_admin_token.startswith("eyJ"), "Токен должен быть валидным JWT"

    def test_movie_data(self, movie_data):
        assert "name" in movie_data, "Должно быть указано имя фильма"
        assert "price" in movie_data, "Должна быть указана цена"
        assert movie_data["price"] > 0, "Цена фильма должна быть больше 0"

    def test_movie_data_keys_and_types(self, movie_data):
        # Проверка, что все ключи присутствуют
        required_keys = ["name", "imageUrl", "price", "description", "location", "published", "genreId"]
        for key in required_keys:
            assert key in movie_data, f"Ключ '{key}' отсутствует в данных фильма"

        # Проверка типов данных
        assert isinstance(movie_data["name"], str), "Название фильма должно быть строкой"
        assert isinstance(movie_data["imageUrl"], str), "URL изображения должен быть строкой"
        assert isinstance(movie_data["price"], int), "Цена должна быть целым числом"
        assert isinstance(movie_data["description"], str), "Описание фильма должно быть строкой"
        assert isinstance(movie_data["location"], str), "Локация должна быть строкой"
        assert isinstance(movie_data["published"], bool), "Поле 'published' должно быть булевым"
        assert isinstance(movie_data["genreId"], int), "ID жанра должен быть целым числом"
