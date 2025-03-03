from Cinescope_API_Movies.all_old_file.movies_api_old import MoviesAPI
from Cinescope_API_Movies.all_old_file.auth_api_old import AuthAPI




class ApiManager:
    """
    Класс для управления API-классами с единой HTTP-сессией.
    """
    def __init__(self, session):

        self.session = session
        self.movies_api = MoviesAPI(session)
        self.auth_api = AuthAPI(session)

































