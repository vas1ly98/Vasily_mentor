# from Cinescope_API_Movies.custom_requester.custom_requester import CustomRequester
# from Cinescope_API_Movies.constants import  BASE_URL
#
#
# class AuthAPI(CustomRequester):
#
#     def __init__(self, session):
#         super().__init__(session=session, base_url=BASE_URL)
#
#     def change_user_role(self, user_id, new_roles,  admin_token):
#         headers = {"Authorization": f"Bearer {admin_token}"}
#         data = {'roles': new_roles}
#         return self.send_request('PATCH', f'user/{user_id}', data=data, headers=headers)
#
#     def get_user(self, user_id, admin_token):
#         headers = {"Authorization": f"Bearer {admin_token}"}
#         response = self.send_request('GET', f'user/{user_id}', headers=headers, expected_status=[200])
#         return response.json()
#
#     def register_user(self, user_data, expected_status=201):
#         """Регистрация нового пользователя. :param user_data: Данные пользователя.:param expected_status: Ожидаемый статус-код."""
#         return self.send_request("POST", 'register', data=user_data, expected_status=expected_status)
#
#     def login_user(self, login_data, expected_status=201):
#         """Авторизует пользователя и получает токен"""
#         return self.send_request("POST", 'login', data=login_data, expected_status=expected_status)
#
#     def delete_user(self, user_id, admin_token, expected_status=204):
#         """Удаляет пользователя (только для ADMIN и SUPER_ADMIN)"""
#         headers = {"Authorization": f"Bearer {admin_token}"}
#         return self.send_request("DELETE",f"/users/{user_id}", headers=headers, expected_status=expected_status)
#
#     #return self.requester.send_request("DELETE", f"/user/{user_id}", headers=headers, expected_status=[200, 204, 404])
#
