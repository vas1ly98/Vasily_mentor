import json
import requests
import logging
import os



class CustomRequester:


    def __init__(self, base_url, session, headers=None):
        self.base_url = base_url
        self.headers = headers or {}
        self.session = session

    def send_request(self, method, endpoint, data=None, params=None, headers = None, expected_status=200):

        url = f"{self.base_url}{endpoint}"

        request_headers = {**self.headers, **(headers or {})}
        response = requests.request(
            method=method,
            url=url,
            headers=request_headers,
            json=data,
            params=params
        )

        self.log_request_and_response(response)

        if response.status_code != expected_status:
            raise ValueError(
                f"Unexpected status code: {response.status_code}. "
                f"Expected: {expected_status}. Response: {response.text}"
            )

        return response

    def log_request_and_response(self, response):
        print("\n======================================== REQUEST ========================================")
        print(f"Method: {response.request.method}")
        print(f"URL: {response.request.url}")
        print(f"Headers: {response.request.headers}")
        if response.request.body:
            print(f"Body: {response.request.body}")
        print("\n======================================== RESPONSE =======================================")
        print(f"Status Code: {response.status_code}")
        print(f"Response Data: {response.text}")

