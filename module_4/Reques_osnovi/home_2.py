# import requests
#
# url = 'https://restful-booker.herokuapp.com/booking'
# payload = {
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
#
# response = requests.post(url, data = payload)
#
# print(response.text)
# print(response.request.body)
#
# import requests
#
# url = "https://httpbin.org/get"
# response = requests.get(url)
#
# print(f"Status Code: {response.status_code}")
# print(f"Headers: {response.headers}")
# print(f"Content (bytes): {response.content}")
# print(f"Text (string): {response.text}")
# print(f"URL: {response.url}")
# print(f"History: {response.history}")
# print(f"Cookies: {response.cookies}")
# print(f"Encoding: {response.encoding}")
# print(f"Elapsed Time: {response.elapsed}")
# print(f"Request: {response.request}")
# print(f"Reason: {response.reason}")