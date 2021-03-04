import requests

BASE_URL = "https://api.nlpcloud.io"
API_VERSION = "v1"


class Client:
    def __init__(self, model, token):
        self.headers = {
            "Authorization": "Token " + token,
        }
        self.root_url = "{}/{}/{}".format(BASE_URL, API_VERSION, model)

    def entities(self, text):
        payload = {
            "text": text
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "entities"), json=payload, headers=self.headers)

        r.raise_for_status()

        return r.json()

    def classification(self, text, labels, multi_class):
        payload = {
            "text": text,
            "labels": labels,
            "multi_class": multi_class
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "classification"), json=payload, headers=self.headers)

        r.raise_for_status()

        return r.json()

    def sentiment(self, text):
        payload = {
            "text": text
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "sentiment"), json=payload, headers=self.headers)

        r.raise_for_status()

        return r.json()

    def question(self, context, question):
        payload = {
            "context": context,
            "question": question
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "question"), json=payload, headers=self.headers)

        r.raise_for_status()

        return r.json()

    def summarization(self, text):
        payload = {
            "text": text
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "summarization"), json=payload, headers=self.headers)

        r.raise_for_status()

        return r.json()

    def dependencies(self, text):
        payload = {
            "text": text
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "dependencies"), json=payload, headers=self.headers)

        r.raise_for_status()

        return r.json()

    def sentence_dependencies(self, text):
        payload = {
            "text": text
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "sentence-dependencies"), json=payload, headers=self.headers)

        r.raise_for_status()

        return r.json()

    def lib_versions(self):
        r = requests.get(
            "{}/{}".format(self.root_url, "versions"), headers=self.headers)

        r.raise_for_status()

        return r.json()
