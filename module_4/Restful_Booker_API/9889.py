# import requests
#
# from module_4.Reques_osnovi.home_3 import session
# from module_4.Reques_osnovi.requestt import booking_id
#
#
# class TestBookings:
#     BASE_URL = "https://restful-booker.herokuapp.com/"
#     HEADERS = {
#         "Content-Type": "application/json",
#         "Accept": "application/json"
#     }
#     json = {
#         "username": "admin",
#         "password": "password123"
#     }
#
#     def get_token(self):
#         response = requests.post(
#             f"{self.BASE_URL}/auth",
#             headers=self.HEADERS,
#             json=self.json
#         )
#         assert response.status_code == 200, "Ошибка авторизации"
#         token = response.json().get("token")
#         assert token is not None, "В ответе не оказалось токена"
#         return token
#
#     def test_create_booking(self):
#         session = requests.Session()
#         session.headers.update({"Cookie": f"token={token}"})
#         booking_data = {
#             "firstname": "Ryan",
#             "lastname": "Gosling",
#             "totalprice": 150000,
#             "depositpaid": True,
#             "bookingdates": {
#                 "checkin": "2024-04-05",
#                 "checkout": "2024-04-08"
#             },
#             "additionalneeds": "Piano"
#         }
#         create_booking = session.post(f"{self.BASE_URL}/booking", json=booking_data)
#         assert create_booking.status_code == 200, "Ошибка при создании брони"
#         booking_id = create_booking.json().get("bookingid")
#         assert booking_id is not None, "Идентификатор брони не найден в ответе"
#         assert create_booking.json()["booking"]["firstname"] == "Ryan", "Заданное имя не совпадает"
#         assert create_booking.json()["booking"]["totalprice"] == 150000, "Заданная стоимость не совпадает"
#         get_booking = session.get(f"{self.BASE_URL}/booking/{booking_id}")
#         assert get_booking.status_code == 200, "Бронь не найдена"
#         assert get_booking.json()["lastname"] == "Gosling", "Заданная фамилия не совпадает"