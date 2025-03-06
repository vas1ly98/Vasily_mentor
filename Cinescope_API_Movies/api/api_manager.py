from Cinescope_API_Movies.api.movies_api import MoviesAPI
from Cinescope_API_Movies.api.auth_api import AuthAPI




class ApiManager:
    """
    Класс для управления API-классами с единой HTTP-сессией.
    """
    def __init__(self, session):

        self.session = session
        self.movies_api = MoviesAPI(session)
        self.auth_api = AuthAPI(session)

































