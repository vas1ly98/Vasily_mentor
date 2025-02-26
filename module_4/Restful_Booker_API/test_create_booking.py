import pytest
from module_4.Restful_Booker_API.constants_booking import BASE_URL
from faker import Faker

faker = Faker()

@pytest.mark.usefixtures("auth_session", "booking_data")
class TestBookings:
    def test_create_booking(self, auth_session, booking_data):
        # Создаём бронирование
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при создании брони"

        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "Идентификатор брони не найден в ответе"
        assert create_booking.json()["booking"]["firstname"] == booking_data["firstname"], "Заданное имя не совпадает"
        assert create_booking.json()["booking"]["totalprice"] == booking_data["totalprice"], "Заданная стоимость не совпадает"

        # Проверяем, что бронирование можно получить по ID
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, "Бронь не найдена"
        assert get_booking.json()["lastname"] == booking_data["lastname"], "Заданная фамилия не совпадает"

        # Удаляем бронирование
        deleted_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert deleted_booking.status_code == 201, "Бронь не удалилась"

        # Проверяем, что бронирование больше недоступно
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 404, "Бронь не удалилась"



    def test_update_booking_with_put(self, auth_session, booking_data):# пример из конспекта метод put
        # Создаём бронирование
        create_response = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_response.status_code == 200, "ошибка при создание брони"

        booking_id = create_response.json().get('bookingid')
        assert booking_id is not None, "Не найден bookingid в ответе"

        # тута мы отправляем пут запрос и меняем данные
        updated_booking_data = {
            "firstname": faker.first_name(),
            "lastname": faker.last_name(),
            "totalprice": faker.random_int(min=100, max=100000),
            "depositpaid": faker.boolean(),
            "bookingdates": {
                "checkin": "2024-06-05",
            "checkout": "2024-06-08"
            },
            "additionalneeds": faker.word()
        }

        put_response = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=updated_booking_data)
        assert put_response.status_code == 200, "Ошибка при обновлении брони"

        # тута мы отправляем гет запрос смотрим что данные обновились
        get_response = auth_session.get(f'{BASE_URL}/booking/{booking_id}')
        assert get_response.status_code == 200, 'Ошибка при получении обновленного бронирования'

        # тута мы проверяем что данные обновились через assert
        booking_data_after_update = get_response.json()
        assert booking_data_after_update == updated_booking_data, 'данные не изменились'

    def test_update_booking_with_patch(self, auth_session, booking_data):# пример из конспекта метод patch
        create_response = auth_session.post(f'{BASE_URL}/booking', json=booking_data)
        assert create_response.status_code == 200, "ошибка при создание брони"

        booking_id = create_response.json().get('bookingid')
        assert booking_id is not None, 'bookingid не найден в ответе'

        update_booking_data = {
            "firstname": 'SANYA',
            "lastname": faker.last_name(),
            "totalprice": faker.random_int(min=100, max=100000),
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-04-05",
                "checkout": "2024-04-08"
            },
            "additionalneeds": "VISKI"
        }

        create_response_patch = auth_session.patch(f'{BASE_URL}/booking/{booking_id}', json=update_booking_data)
        assert create_response_patch.status_code == 200, "Ошибка при обновлении брони"

        get_response = auth_session.get(f'{BASE_URL}/booking/{booking_id}')
        assert get_response.status_code == 200, "Ошибка при получение запроса"

        booking_data_after_update = get_response.json()
        assert booking_data_after_update['firstname'] == update_booking_data['firstname'], 'Данные не изменились'
        assert booking_data_after_update['additionalneeds'] == update_booking_data[
            'additionalneeds'], 'данные не изменились'


