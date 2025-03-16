from Cinescope_API_Movies.api.movies_api import MoviesAPI
from Cinescope_API_Movies.api.auth_api import AuthAPI
from Cinescope_API_Movies.api.user_api import UserAPI



class ApiManager:
    """
    Класс для управления API-классами с единой HTTP-сессией.
    """
    def __init__(self, session):

        self.session = session
        self.movies_api = MoviesAPI(session)
        self.auth_api = AuthAPI(session)
        self.user_api = UserAPI(session)

    def close_session(self):
        self.session.close()

































