from Cinescope_API_Movies.constants import MOVIES_ENDPOINT, MOVIES_GENRES_ENDPOINT
import pytest
import requests
from Cinescope_API_Movies.custom_requester.custom_requester import CustomRequester
from Cinescope.api.api_manager import  ApiManager
import time
from Cinescope_API_Movies.api.api_manager import ApiManager
from Cinescope_API_Movies.api.movies_api import MoviesAPI
from Cinescope_API_Movies.conftest import api_manager


class TestFilmApi:

    def test_get_all_movies(self, api_manager):
        response = api_manager.movies_api.get_movies()
        assert response.status_code == 200
        assert "movies" in response.json()

    def test_filter_movies_by_price(self, api_manager):
        response = api_manager.movies_api.get_movies(params={"minPrice": 100, "maxPrice": 500})
        assert response.status_code == 200
        for movie in response.json()["movies"]:
            assert 100 <= movie["price"] <= 500








