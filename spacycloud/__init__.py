import requests

BASE_URL = "https://api.spacycloud.io"
API_VERSION = "v1"


class Client:
    def __init__(self, model, token):
        self.headers = {
            "Authorization": "Token " + token,
        }
        self.root_url = "{}/{}/{}".format(BASE_URL, API_VERSION, model)

    def _api_post(self, endpoint, user_input):
        payload = {
            "text": user_input
        }

        r = requests.post(
            "{}/{}".format(self.root_url, endpoint), json=payload, headers=self.headers)

        r.raise_for_status()

        return r.json()

    def _api_get(self, endpoint):
        r = requests.get(
            "{}/{}".format(self.root_url, endpoint), headers=self.headers)

        r.raise_for_status()

        return r.json()

    def entities(self, user_input):
        return self._api_post("entities", user_input)

    def dependencies(self, user_input):
        return self._api_post("dependencies", user_input)

    def sentence_dependencies(self, user_input):
        return self._api_post("sentence-dependencies", user_input)

    def lib_versions(self):
        return self._api_get("version")
