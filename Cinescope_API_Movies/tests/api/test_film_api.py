from Cinescope_API_Movies.constants import MOVIES_ENDPOINT, MOVIES_GENRES_ENDPOINT
import pytest
import requests
from Cinescope_API_Movies.custom_requester.custom_requester import CustomRequester
from Cinescope.api.api_manager import  ApiManager
import time
from Cinescope_API_Movies.api.api_manager import ApiManager
from Cinescope_API_Movies.api.movies_api import MoviesAPI
from Cinescope_API_Movies.conftest import api_manager, create_movie, super_admin_token
from module_4.Reques_osnovi.home_1 import response_data


class TestFilmApi:

    def test_get_all_movies(self, api_manager):
        response = api_manager.movies_api.get_movies()
        assert "movies" in response.json()

    def test_filter_movies_by_price(self, api_manager):
        response = api_manager.movies_api.get_movies(params={"minPrice": 100, "maxPrice": 500})
        for movie in response.json()["movies"]:
            assert 100 <= movie["price"] <= 500

    def test_create_movies(self, api_manager, super_admin_token, movie_data):


       response = api_manager.movies_api.create_movie(movie_data, super_admin_token)
       response_name = response.json()['name']


    def test_delete_movies(self, api_manager, create_movie):
        movies_id = create_movie
        response = api_manager.movies_api.delete_movie(movies_id, super_admin_token)
        assert response.status_code == 204

    #def test_get_films(self, api_manager):
       # response = api_manager.movies_api.get_movies()
       # assert response.status_code == 200
       # movies = response.json()
       # movie_names = [movie['name'] for movie in movies]
        #assert response_name not in movie_names




