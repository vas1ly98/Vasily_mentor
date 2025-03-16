import time
from Cinescope_API_Movies.conftest import api_manager, create_movie, super_admin_token


class TestFilmApi:

    def test_get_all_movies(self, api_manager):
        response = api_manager.movies_api.get_movies()
        assert "movies" in response.json()

    def test_filter_movies_by_price(self, api_manager):
        response = api_manager.movies_api.get_movies(params={"minPrice": 100, "maxPrice": 500})
        for movie in response.json()["movies"]:
            assert 100 <= movie["price"] <= 500

    def test_create_movies(self, api_manager, create_movie):
       movie_id = create_movie["id"]
       movie_name = create_movie["name"]
       assert movie_id is not None, "ID не может быть пустым"

       movie_response = api_manager.movies_api.get_movie(movie_id)
       assert movie_response.status_code ==200, 'Не найден id'
       assert movie_response.json()["name"] == movie_name, 'Имя фильма не совпадает'

    #дз
    def test_create_movies_negative(self, api_manager, create_movie):
       movie_id = create_movie["id"]
       movie_name = create_movie["name"]
       assert movie_id is not None, "ID не может быть пустым"

       movie_response = api_manager.movies_api.get_movie(movie_id)
       assert movie_response.status_code ==200, 'Не найден id'
       assert movie_response.json()["name"] == movie_name, 'Имя фильма не совпадает'


    def test_delete_movies(self, api_manager, super_admin_token, create_movie):
        movies_id = create_movie['id']
        response = api_manager.movies_api.delete_movie(movies_id, super_admin_token)
        assert response.status_code == 200, f"Ошибка: фильм не был удалён. Ответ: {response.json()}"
        time.sleep(2)

        get_response = api_manager.movies_api.get_movie(movies_id, expected_status=404)
        assert get_response.status_code == 404, "Ошибка: фильм всё ещё существует после удаления"






