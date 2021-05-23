import os
import requests
import json


class APIInterface:
    @staticmethod
    def post(route, data=None):
        url = route
        # print(f"url = {url}, data = {data}")
        # headers = {
        #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
        # }
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0"
        }
        response = requests.post(url, json=data, headers=headers)
        if response.status_code != 200:
            raise Exception(
                f"Call to {route} failed with {response.status_code} and response {response.text}"
            )
        return response.text

    @staticmethod
    def get(route, params=None):
        url = route
        # print(f"url = {url}, params = {params}")
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
        }
        response = requests.get(url, params=params, headers=headers)
        if response.status_code != 200:
            raise Exception(
                f"Call to {route} failed with {response.status_code} and response {response.text}"
            )
        return response.text

    @staticmethod
    def put(route, data=None):
        url = route
        # print(f"url = {url}, data = {data}")
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
        }
        response = requests.put(url, json=data, headers=headers)
        if response.status_code != 200:
            raise Exception(
                f"Call to {route} failed with {response.status_code} and response {response.text}"
            )
        return response.text
