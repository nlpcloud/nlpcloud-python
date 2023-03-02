import requests
from requests.models import HTTPError

BASE_URL = "https://api.nlpcloud.io"
API_VERSION = "v1"


class Client:
    def __init__(self, model, token, gpu=False, lang="", asynchronous=False):
        self.headers = {
            "Authorization": "Token " + token,
            "User-Agent": "nlpcloud-python-client"
        }

        self.root_url = f"{BASE_URL}/{API_VERSION}/"

        if lang == "en":
            lang = ""

        if gpu:
            self.root_url += "gpu/"

        if asynchronous:
            self.root_url += "async/"

        if lang:
            self.root_url += lang + "/"

        self.root_url += model

    def ad_generation(self, keywords):
        payload = {
            "keywords": keywords
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "ad-generation"), json=payload, headers=self.headers)

        try:
            r.raise_for_status()
        except HTTPError as err:
            if "<!DOCTYPE html>" in r.text:
                raise HTTPError(str(err))

            raise HTTPError(str(err) + ": " + str(r.text))

        return r.json()

    def article_generation(self, title):
        payload = {
            "title": title
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "article-generation"), json=payload, headers=self.headers)

        try:
            r.raise_for_status()
        except HTTPError as err:
            raise HTTPError(str(err) + ": " + str(r.text))

        return r.json()

    def asr(self, url=None, encoded_file=None, input_language=None):
        payload = {
            "url": url,
            "encoded_file": encoded_file,
            "input_language": input_language
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "asr"), json=payload, headers=self.headers)

        try:
            r.raise_for_status()
        except HTTPError as err:
            if "<!DOCTYPE html>" in r.text:
                raise HTTPError(str(err))

            raise HTTPError(str(err) + ": " + str(r.text))

        return r.json()

    def async_result(self, url):
        r = requests.get(url, headers=self.headers)

        try:
            r.raise_for_status()
        except HTTPError as err:
            raise HTTPError(str(err) + ": " + str(r.text))

        return r.json()

    def chatbot(self, text, context=None, history=None):
        payload = {
            "input": text,
            "context": context,
            "history": history
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "chatbot"), json=payload, headers=self.headers)

        try:
            r.raise_for_status()
        except HTTPError as err:
            if "<!DOCTYPE html>" in r.text:
                raise HTTPError(str(err))

            raise HTTPError(str(err) + ": " + str(r.text))

        return r.json()

    def classification(self, text, labels=None, multi_class=None):
        payload = {
            "text": text,
            "labels": labels,
            "multi_class": multi_class
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "classification"), json=payload, headers=self.headers)

        try:
            r.raise_for_status()
        except HTTPError as err:
            if "<!DOCTYPE html>" in r.text:
                raise HTTPError(str(err))

            raise HTTPError(str(err) + ": " + str(r.text))

        return r.json()

    def code_generation(self, instruction):
        payload = {
            "instruction": instruction
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "code-generation"), json=payload, headers=self.headers)

        try:
            r.raise_for_status()
        except HTTPError as err:
            raise HTTPError(str(err) + ": " + str(r.text))

        return r.json()

    def dependencies(self, text):
        payload = {
            "text": text
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "dependencies"), json=payload, headers=self.headers)

        try:
            r.raise_for_status()
        except HTTPError as err:
            if "<!DOCTYPE html>" in r.text:
                raise HTTPError(str(err))

            raise HTTPError(str(err) + ": " + str(r.text))

        return r.json()

    def embeddings(self, sentences):
        payload = {
            "sentences": sentences
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "embeddings"), json=payload, headers=self.headers)

        try:
            r.raise_for_status()
        except HTTPError as err:
            if "<!DOCTYPE html>" in r.text:
                raise HTTPError(str(err))

            raise HTTPError(str(err) + ": " + str(r.text))

        return r.json()

    def entities(self, text, searched_entity=None):
        payload = {
            "text": text,
            "searched_entity": searched_entity
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "entities"), json=payload, headers=self.headers)

        try:
            r.raise_for_status()
        except HTTPError as err:
            if "<!DOCTYPE html>" in r.text:
                raise HTTPError(str(err))

            raise HTTPError(str(err) + ": " + str(r.text))

        return r.json()

    def generation(self, text, min_length=None, max_length=None, length_no_input=None,
                   end_sequence=None, remove_input=None, do_sample=None, num_beams=None, early_stopping=None,
                   no_repeat_ngram_size=None, num_return_sequences=None, top_k=None, top_p=None,
                   temperature=None, repetition_penalty=None, length_penalty=None, bad_words=None, remove_end_sequence=None):
        payload = {
            "text": text,
            "min_length": min_length,
            "max_length": max_length,
            "length_no_input": length_no_input,
            "end_sequence": end_sequence,
            "remove_input": remove_input,
            "do_sample": do_sample,
            "num_beams": num_beams,
            "early_stopping": early_stopping,
            "no_repeat_ngram_size": no_repeat_ngram_size,
            "num_return_sequences": num_return_sequences,
            "top_k": top_k,
            "top_p": top_p,
            "temperature": temperature,
            "repetition_penalty": repetition_penalty,
            "length_penalty": length_penalty,
            "bad_words": bad_words,
            "remove_end_sequence": remove_end_sequence
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "generation"), json=payload, headers=self.headers)

        try:
            r.raise_for_status()
        except HTTPError as err:
            if "<!DOCTYPE html>" in r.text:
                raise HTTPError(str(err))

            raise HTTPError(str(err) + ": " + str(r.text))

        return r.json()

    def gs_correction(self, text):
        payload = {
            "text": text
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "gs-correction"), json=payload, headers=self.headers)

        try:
            r.raise_for_status()
        except HTTPError as err:
            raise HTTPError(str(err) + ": " + str(r.text))

        return r.json()

    def image_generation(self, text):
        payload = {
            "text": text
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "image-generation"), json=payload, headers=self.headers)

        try:
            r.raise_for_status()
        except HTTPError as err:
            raise HTTPError(str(err) + ": " + str(r.text))

        return r.json()

    def intent_classification(self, text):
        payload = {
            "text": text
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "intent-classification"), json=payload, headers=self.headers)

        try:
            r.raise_for_status()
        except HTTPError as err:
            raise HTTPError(str(err) + ": " + str(r.text))

        return r.json()

    def kw_kp_extraction(self, text):
        payload = {
            "text": text
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "kw-kp-extraction"), json=payload, headers=self.headers)

        try:
            r.raise_for_status()
        except HTTPError as err:
            raise HTTPError(str(err) + ": " + str(r.text))

        return r.json()

    def langdetection(self, text):
        payload = {
            "text": text
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "langdetection"), json=payload, headers=self.headers)

        try:
            r.raise_for_status()
        except HTTPError as err:
            if "<!DOCTYPE html>" in r.text:
                raise HTTPError(str(err))

            raise HTTPError(str(err) + ": " + str(r.text))

        return r.json()

    def lib_versions(self):
        r = requests.get(
            "{}/{}".format(self.root_url, "versions"), headers=self.headers)

        try:
            r.raise_for_status()
        except HTTPError as err:
            if "<!DOCTYPE html>" in r.text:
                raise HTTPError(str(err))

            raise HTTPError(str(err) + ": " + str(r.text))

        return r.json()

    def paraphrasing(self, text):
        payload = {
            "text": text
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "paraphrasing"), json=payload, headers=self.headers)

        try:
            r.raise_for_status()
        except HTTPError as err:
            if "<!DOCTYPE html>" in r.text:
                raise HTTPError(str(err))

            raise HTTPError(str(err) + ": " + str(r.text))

        return r.json()

    def question(self, question, context=None):
        payload = {
            "question": question,
            "context": context
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "question"), json=payload, headers=self.headers)

        try:
            r.raise_for_status()
        except HTTPError as err:
            if "<!DOCTYPE html>" in r.text:
                raise HTTPError(str(err))

            raise HTTPError(str(err) + ": " + str(r.text))

        return r.json()

    def semantic_search(self, text, num_results=None):
        payload = {
            "text": text,
            "num_results": num_results
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "semantic-search"), json=payload, headers=self.headers)

        try:
            r.raise_for_status()
        except HTTPError as err:
            if "<!DOCTYPE html>" in r.text:
                raise HTTPError(str(err))

            raise HTTPError(str(err) + ": " + str(r.text))

        return r.json()

    def semantic_similarity(self, sentences):
        payload = {
            "sentences": sentences
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "semantic-similarity"), json=payload, headers=self.headers)

        try:
            r.raise_for_status()
        except HTTPError as err:
            if "<!DOCTYPE html>" in r.text:
                raise HTTPError(str(err))

            raise HTTPError(str(err) + ": " + str(r.text))

        return r.json()

    def sentence_dependencies(self, text):
        payload = {
            "text": text
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "sentence-dependencies"), json=payload, headers=self.headers)

        try:
            r.raise_for_status()
        except HTTPError as err:
            if "<!DOCTYPE html>" in r.text:
                raise HTTPError(str(err))

            raise HTTPError(str(err) + ": " + str(r.text))

        return r.json()

    def sentiment(self, text):
        payload = {
            "text": text
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "sentiment"), json=payload, headers=self.headers)

        try:
            r.raise_for_status()
        except HTTPError as err:
            raise HTTPError(str(err) + ": " + str(r.text))

        return r.json()

    def summarization(self, text, size=None):
        payload = {
            "text": text,
            "size": size
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "summarization"), json=payload, headers=self.headers)

        try:
            r.raise_for_status()
        except HTTPError as err:
            if "<!DOCTYPE html>" in r.text:
                raise HTTPError(str(err))

            raise HTTPError(str(err) + ": " + str(r.text))

        return r.json()

    def tokens(self, text):
        payload = {
            "text": text
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "tokens"), json=payload, headers=self.headers)

        try:
            r.raise_for_status()
        except HTTPError as err:
            if "<!DOCTYPE html>" in r.text:
                raise HTTPError(str(err))

            raise HTTPError(str(err) + ": " + str(r.text))

        return r.json()

    def translation(self, text, source, target):
        payload = {
            "text": text,
            "source": source,
            "target": target
        }

        r = requests.post(
            "{}/{}".format(self.root_url, "translation"), json=payload, headers=self.headers)

        try:
            r.raise_for_status()
        except HTTPError as err:
            if "<!DOCTYPE html>" in r.text:
                raise HTTPError(str(err))

            raise HTTPError(str(err) + ": " + str(r.text))

        return r.json()
