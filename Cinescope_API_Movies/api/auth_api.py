from Cinescope_API_Movies.custom_requester.custom_requester import CustomRequester
from Cinescope_API_Movies.constants import  BASE_URL
from Cinescope_API_Movies.enums.roles import Roles
from Modul_4.Cinescope.models.base_models import TestUser
import json



class AuthAPI(CustomRequester):

    def __init__(self, session):
        super().__init__(session=session, base_url=BASE_URL)


    def register_user(self, user_data: TestUser):
        """Регистрирует нового пользователя"""
        return self.send_request("POST", "register", data=json.loads(user_data.model_dump_json(exclude_unset=True)))

    def login_user(self, login_data):
        """Авторизует пользователя и получает токен"""
        return self.send_request("POST", "login", data=login_data)

    def change_user_role(self, user_id, new_roles, admin_token):
        """Изменяет роль пользователя"""
        headers = {"Authorization": f"Bearer {admin_token}"}
        data = {"roles": new_roles}
        return self.send_request("PATCH", f"/user/{user_id}", data=data, headers=headers)

    def delete_user(self, user_id, admin_token):
        """Удаляет пользователя (только для ADMIN и SUPER_ADMIN)"""
        headers = {"Authorization": f"Bearer {admin_token}"}
        return self.send_request("DELETE", f"/user/{user_id}", headers=headers, expected_status=[200, 204, 404])

    def get_user(self, user_id, admin_token):
        """Получение информации о пользователе."""
        headers = {"Authorization": f"Bearer {admin_token}"}
        response = self.send_request("GET", f"user/{user_id}", headers=headers, expected_status=[200])
        return response.json()

