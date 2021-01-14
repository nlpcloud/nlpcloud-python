import requests

BASE_URL = "https://api.spacycloud.io"
API_VERSION = "v1"


class Client:
    def __init__(self, token):
        self.headers = {
            "Authorization": "Token " + token,
        }
        self.root_url = "{}/{}".format(BASE_URL, API_VERSION)

    def _call_api(self, endpoint, model, user_input):
        payload = {
            "text": user_input
        }

        r = requests.post(
            "{}/{}/endpoint".format(self.root_url, model), json=payload, headers=self.headers)

        return r.json()

    def entities(self, model, user_input):
        return self._call_api("entities", model, user_input)

    def dependencies(self, model, user_input):
        return self._call_api("dependencies", model, user_input)

    def sentence_dependencies(self, model, user_input):
        return self._call_api("sentence_dependencies", model, user_input)
