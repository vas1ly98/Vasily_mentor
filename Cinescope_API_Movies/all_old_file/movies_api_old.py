from Cinescope_API_Movies.custom_requester.custom_requester import CustomRequester
from Cinescope_API_Movies.constants import base_url



class MoviesAPI(CustomRequester):

    def __init__(self, session):
        super().__init__(session=session, base_url=base_url)


    def get_movies(self, params = None):
        return self.send_request('GET', 'movies', params=params, expected_status=self.SC_OK)

    def get_movie(self, movie_id, expected_status=None):
        if expected_status is None:
            expected_status = self.SC_OK
        return self.send_request('GET', f'movies/{movie_id}', expected_status= expected_status)

    def create_movie(self, data, token):
        headers = {"Authorization": f"Bearer {token}"}
        return self.send_request('POST', 'movies', data=data, headers=headers, expected_status=self.SC_OK)

    def delete_movie(self, movie_id, token, expected_status=None):
        if expected_status is None:
            expected_status = self.SC_OK
        headers = {"Authorization": f"Bearer {token}"}
        return self.send_request('DELETE', f'movies/{movie_id}', headers=headers, expected_status=expected_status)





































