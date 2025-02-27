from Cinescope_API_Movies.custom_requester.custom_requester import CustomRequester
from Cinescope_API_Movies.constants import MOVIES_ENDPOINT, MOVIES_GENRES_ENDPOINT, base_url, headers
from Cinescope.constants import BASE_URL



class MoviesAPI(CustomRequester):

    def __init__(self, requester, session):
        self.requester = requester
        super().__init__(session=session, base_url=BASE_URL)





    def get_movies(self, params = None):
        return self.requester.send_request('GET', 'movies', params=params, expected_status=self.SC_OK)

    def get_movie(self, movie_id):
        return self.requester.send_request('GET', 'movies/{movie_id}', expected_status=self.SC_OK)

    def create_movie(self, data, token):
        headers = {"Authorization": f"Bearer {token}"}
        return self.requester.send_request('POST', 'movies', data=data, headers=headers, expected_status=self.SC_OK)

    def delete_movie(self, movie_id, token):
        headers = {"Authorization": f"Bearer {token}"}
        return self.requester.send_request('DELETE', 'movies/{movie_id}', headers=headers)





































