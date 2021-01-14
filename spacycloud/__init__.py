import requests


class Client:
    def __init__(self, token):
        self.token = token

    def get(self, user_input):

        headers = {
            "Authorization": "Token " + self.token,
        }

        payload = {
            "text": user_input
        }

        r = requests.post(
            "https://api.spacycloud.io/v1/en_core_web_sm/entities", json=payload, headers=headers)

        print(r.text)
