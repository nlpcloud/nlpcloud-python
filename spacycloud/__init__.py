import requests


class Client:
    def __init__(self, token):
        self.headers = {
            "Authorization": "Token " + token,
        }

    def entities(self, user_input):
        payload = {
            "text": user_input
        }

        r = requests.post(
            "https://api.spacycloud.io/v1/en_core_web_sm/entities", json=payload, headers=self.headers)

        return r.json()

    def dependencies(self, user_input):
        payload = {
            "text": user_input
        }

        r = requests.post(
            "https://api.spacycloud.io/v1/en_core_web_sm/dependencies", json=payload, headers=self.headers)

        return r.json()

    def sentence_dependencies(self, user_input):
        payload = {
            "text": user_input
        }

        r = requests.post(
            "https://api.spacycloud.io/v1/en_core_web_sm/sentence-dependencies", json=payload, headers=self.headers)

        return r.json()
