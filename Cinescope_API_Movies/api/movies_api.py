from Cinescope_API_Movies.custom_requester.custom_requester import CustomRequester
from Cinescope_API_Movies.constants import MOVIES_ENDPOINT, MOVIES_GENRES_ENDPOINT, base_url, headers


class MoviesAPI(CustomRequester):

    def __init__(self, requester, session):
        self.requester = requester
        super().__init__(session=session, base_url=base_url)





    def get_movies(self, params = None):
        return self.requester.send_request('GET', f'{self.base_url}/movies', params=params)

    def get_movie(self, movie_id):
        return self.requester.send_request('GET', f'{self.base_url}/movies/{movie_id}')

    def create_movie(self, data, token):
        headers = {"Authorization": f"Bearer {token}"}
        return self.requester.send_request('POST', f'{self.base_url}/movies', data=data, headers=headers)

    def delete_movie(self, movie_id, token):
        headers = {"Authorization": f"Bearer {token}"}
        return self.requester.send_request('DELETE', f'{base_url}/movies{movie_id}', headers=headers)



