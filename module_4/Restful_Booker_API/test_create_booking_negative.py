# import pytest
# from module_4.Restful_Booker_API.constants_booking import BASE_URL
# from faker import Faker
# from module_4.Reques_osnovi.requestt import booking_id
#
# faker = Faker()
#
# @pytest.mark.usefixtures("auth_session", "booking_data")
# class TestBookings:
#     def test_create_booking(self, auth_session, booking_data):
#         # Создаём бронирование
#         create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
#         assert create_booking.status_code == 200, "Ошибка при создании брони"
#
#         booking_id = create_booking.json().get("bookingid")
#         assert booking_id is not None, "Идентификатор брони не найден в ответе"
#         assert create_booking.json()["booking"]["firstname"] == booking_data["firstname"], "Заданное имя не совпадает"
#         assert create_booking.json()["booking"]["totalprice"] == booking_data["totalprice"], "Заданная стоимость не совпадает"
#
#         # Проверяем, что бронирование можно получить по ID
#         get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
#         assert get_booking.status_code == 200, "Бронь не найдена"
#         assert get_booking.json()["lastname"] == booking_data["lastname"], "Заданная фамилия не совпадает"
#
#         # Удаляем бронирование
#         deleted_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
#         assert deleted_booking.status_code == 201, "Бронь не удалилась"
#
#         # Проверяем, что бронирование больше недоступно
#         get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
#         assert get_booking.status_code == 404, "Бронь не удалилась"
#
#     # тут короче сервер походу не обрабатывает такие ошибки и 500 выдает вроде все правильно(негативная проверка с post)
#     def test_create_booking_with_invalid_data_post(self, auth_session):  # негативная проверка # 1
#         update_booking_data = {
#             "firstname": 123,
#             "lastname": faker.last_name(),
#             "totalprice": faker.random_int(min=100, max=100000),
#             "depositpaid": 'asfa',
#             "bookingdates": {
#                 "checkin": "2024-04-05",
#                 "checkout": "2024-04-08"
#             },
#             "additionalneeds": "VISKI"
#         }
#
#         create_response = auth_session.post(f'{BASE_URL}/booking', json=update_booking_data)
#         print(f"Status Code: {create_response.status_code}")
#         print(f"Response Text: {create_response.text}")
#
#         # Делаем проверку на ошибку
#         assert create_response.status_code == 400, f'Ошибка при вводе данных: {create_response.text}'
#         assert "error" in create_response.json(), f"Ответ не содержит сообщение об ошибке: {create_response.json()}"
#
#
#
#     def test_update_booking_with_patch(self, auth_session, booking_data):  # негативная проверка # 2 patch
#         create_response = auth_session.post(f'{BASE_URL}/booking', json=booking_data)
#         assert create_response.status_code == 200, "ошибка при создание брони"
#
#         booking_id = 98796
#         update_booking_data = {
#             "firstname": 'SANYA',
#         }
#
#         create_response_patch = auth_session.patch(f'{BASE_URL}/booking/{booking_id }', json=update_booking_data)
#         assert create_response_patch.status_code == 404, "должна быть 404"
#
#
