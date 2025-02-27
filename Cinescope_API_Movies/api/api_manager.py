from Cinescope_API_Movies.api.movies_api import MoviesAPI
from Cinescope_API_Movies.constants import base_url
from Cinescope_API_Movies.custom_requester.custom_requester import CustomRequester
from Cinescope_API_Movies.api.auth_api import AuthAPI




class ApiManager:
    """
    Класс для управления API-классами с единой HTTP-сессией.
    """
    def __init__(self, session):

        self.session = session
        self.requester = CustomRequester(session=session, base_url=base_url)
        self.movies_api = MoviesAPI(self.requester, session)
        self.auth_api = AuthAPI(session)

































