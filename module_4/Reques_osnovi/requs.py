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
# print(response.json())