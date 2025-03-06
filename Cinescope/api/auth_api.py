from Cinescope.custom_requester.custom_requester import CustomRequester


class AuthAPI(CustomRequester):



    def __init__(self, session):
        super().__init__(session=session, base_url=BASE_URL)

    def register_user(self, user_data, expected_status=201):
        """
        Регистрация нового пользователя.
        :param user_data: Данные пользователя.
        :param expected_status: Ожидаемый статус-код.
        """
        return self.send_request(
            method="POST",
            endpoint=REGISTER_ENDPOINT,
            data=user_data,
            expected_status=expected_status
        )

    def login_user(self, login_data, expected_status=201):
        """
        Авторизация пользователя.
        :param login_data: Данные для логина.
        :param expected_status: Ожидаемый статус-код.
        """
        return self.send_request(
            method="POST",
            endpoint=LOGIN_ENDPOINT,
            data=login_data,
            expected_status=expected_status
        )

    def delete_user(self, user_id, expected_status=204):
        """
        Удаление пользователя.
        :param user_id: ID пользователя.
        :param expected_status: Ожидаемый статус-код.
        """
        return self.send_request(
            method="DELETE",
            endpoint=f"/users/{user_id}",
            expected_status=expected_status
        )

