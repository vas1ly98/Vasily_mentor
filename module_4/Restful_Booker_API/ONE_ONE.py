# import requests
#
# BASE_URL = "https://restful-booker.herokuapp.com/"
# HEADERS = {
#     "Content-Type": "application/json",
#     "Accept": "application/json"
# }
# json_data = {
#     "username": "admin",
#     "password": "password123"
# }
#
# response = requests.post(f"{BASE_URL}/auth", headers=HEADERS, json=json_data)
#
# print("Статус код ответа:", response.status_code)
# print("Ответ сервера:", response.json())  # Посмотри, что сервер вернёт!