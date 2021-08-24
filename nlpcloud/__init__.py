import requests

BASE_URL = "https://api.nlpcloud.io"
API_VERSION = "v1"


class Client:
    def __init__(self, model, token, gpu=False):
        self.headers = {
            "Authorization": "Token " + token,
            "User-Agent": "nlpcloud-python-client"
        }
        if gpu:
            self.root_url = "{}/{}/gpu/{}".format(BASE_URL, API_VERSION, model)
        else:
            self.root_url = "{}/{}/{}".format(BASE_URL, API_VERSION, model)

    def entities(self, text):
        payload = {
            "text": text
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "entities"), json=payload, headers=self.headers)

        r.raise_for_status()

        return r.json()

    def classification(self, text, labels, multi_class=None):
        payload = {
            "text": text,
            "labels": labels,
            "multi_class": multi_class
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "classification"), json=payload, headers=self.headers)

        r.raise_for_status()

        return r.json()

    def generation(self, text, min_length=None, max_length=None, length_no_input=None,
                   end_sequence=None, remove_input=None, top_k=None, top_p=None,
                   temperature=None, repetition_penalty=None, length_penalty=None):
        payload = {
            "text": text,
            "min_length": min_length,
            "max_length": max_length,
            "length_no_input": length_no_input,
            "end_sequence": end_sequence,
            "remove_input": remove_input,
            "top_k": top_k,
            "top_p": top_p,
            "temperature": temperature,
            "repetition_penalty": repetition_penalty,
            "length_penalty": length_penalty
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "generation"), json=payload, headers=self.headers)

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

    def translation(self, text):
        payload = {
            "text": text
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "translation"), json=payload, headers=self.headers)

        r.raise_for_status()

        return r.json()

    def langdetection(self, text):
        payload = {
            "text": text
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "langdetection"), json=payload, headers=self.headers)

        r.raise_for_status()

        return r.json()

    def tokens(self, text):
        payload = {
            "text": text
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "tokens"), json=payload, headers=self.headers)

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
