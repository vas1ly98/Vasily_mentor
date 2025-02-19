import requests
from constants import BASE_URL, HEADERS  # Импортируем константы

class TestBookings:

    json = {
        "username": "admin",
        "password": "password123"
    }

    def get_token(self):
        response = requests.post(
            f"{BASE_URL}/auth",  # Используем BASE_URL напрямую
            headers=HEADERS,
            json=self.json
        )
        assert response.status_code == 200, "Ошибка авторизации"
        token = response.json().get("token")
        assert token is not None, "В ответе не оказалось токена"
        return token

    def test_create_booking(self):
        session = requests.Session()
        session.headers.update(HEADERS)  # Убираем self

        # Получаем токен авторизации
        token = self.get_token()
        session.headers.update({"Cookie": f"token={token}"})

        # Данные для бронирования
        booking_data = {
            "firstname": "Ryan",
            "lastname": "Gosling",
            "totalprice": 150000,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-04-05",
                "checkout": "2024-04-08"
            },
            "additionalneeds": "Piano"
        }

        # Создаём бронирование
        create_booking = session.post(f"{BASE_URL}/booking", json=booking_data)  # Убираем self
        assert create_booking.status_code == 200, "Ошибка при создании брони"

        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "Идентификатор брони не найден в ответе"

        # Проверяем, что бронирование можно получить по ID
        get_booking = session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, "Бронь не найдена"
        assert get_booking.json()["lastname"] == "Gosling", "Заданная фамилия не совпадает"

        # Удаляем бронирование
        deleted_booking = session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert deleted_booking.status_code == 201, "Бронь не удалилась"

        # Проверяем, что бронирование больше недоступно
        get_booking = session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 404, "Бронь не удалилась"
