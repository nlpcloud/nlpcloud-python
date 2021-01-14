import requests

BASE_URL = "https://api.spacycloud.io"
API_VERSION = "v1"


class Client:
    def __init__(self, model, token):
        self.headers = {
            "Authorization": "Token " + token,
        }
        self.root_url = "{}/{}/{}".format(BASE_URL, API_VERSION, model)

    def _call_api(self, endpoint, user_input):
        payload = {
            "text": user_input
        }

        r = requests.post(
            "{}/{}".format(self.root_url, endpoint), json=payload, headers=self.headers)

        r.raise_for_status()

        return r.json()

    def entities(self, user_input):
        return self._call_api("entities", user_input)

    def dependencies(self, user_input):
        return self._call_api("dependencies", user_input)

    def sentence_dependencies(self, user_input):
        return self._call_api("sentence_dependencies", user_input)

    def lib_versions(self):
        r = requests.get(
            "{}/version".format(self.root_url), headers=self.headers)

        r.raise_for_status()

        return r.json()
