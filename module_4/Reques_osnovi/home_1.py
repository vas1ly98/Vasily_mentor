# import requests
#
# # делаем словарь для отправки
# data = {
#     "firstname": "Jim",
#     "lastname": "Brown",
#     "totalprice": 111,
#     "depositpaid": True,
#     "bookingdates": {
#         "checkin": "2025-01-04",
#         "checkout": "2025-01-15"
#     },
#     "additionalneeds": "Breakfast"
# }
# URL = 'https://restful-booker.herokuapp.com/booking'
# # отправляем наш запрос
#
# response = requests.post(URL, json=data)
#
# assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
#
# response_data = response.json()
# assert "bookingid" in response_data, "Response JSON does not contain 'bookingid'"
#
# booking_id = response_data["bookingid"]
#
# response_get = requests.get(f"{URL}/{booking_id}")
# assert response_get.status_code == 200, f"Expected 200, but got {response_get.status_code}"
#
# response_get_data = response_get.json()
# assert response_get_data["firstname"] == data["firstname"], "Firstname does not match"
# assert response_get_data["lastname"] == data["lastname"], "Lastname does not match"
#
# print("Тест успешно выполнен!")

