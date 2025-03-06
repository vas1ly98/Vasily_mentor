from Cinescope.custom_requester.custom_requester import CustomRequester


class UserAPI(CustomRequester):
    """
    Класс для работы с API пользователей.
    """
    def __init__(self, session):
        super().__init__(session=session, base_url=BASE_URL)  # Передаем BASE_URL правильно
        self.session = session

    def get_user_info(self, user_id, expected_status=200):
        """
        Получение информации о пользователе.
        :param user_id: ID пользователя.
        :param expected_status: Ожидаемый статус-код.
        """
        return self.send_request(
            method="GET",
            endpoint=f"/users/{user_id}",
            expected_status=expected_status
        )

