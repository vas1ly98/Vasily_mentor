import requests

booking_id = 1
response = requests.get(f'https://restful-booker.herokuapp.com/booking/{booking_id}')

data = response.json()

# Тело ответа в словаре
print(f"Тело ответа: {data}")