# Python Client For NLP Cloud

This is a Python client for the NLP Cloud API: https://docs.nlpcloud.io

NLP Cloud serves all the spaCy pre-trained models, and your own custom models, through a RESTful API, so it's easy for you to use them in production.

If you face an issue, don't hesitate to raise it as a Github issue. Thanks!

## Installation

Install via pip.

```shell
pip install nlpcloud
```

## Examples

Here is a full example that uses the `en_core_web_sm` model, with a fake token:

```python
import nlpcloud

client = nlpcloud.Client("en_core_web_sm", "4eC39HqLyjWDarjtT1zdp7dc")
client.entities("John Doe is a Go Developer at Google")
```

And a full example that uses your own custom model `7894`:

```python
import nlpcloud

client = nlpcloud.Client("custom_model/7894", "4eC39HqLyjWDarjtT1zdp7dc")
client.entities("John Doe is a Go Developer at Google")
```

A json object is returned. Here is what it could look like:

```json
[
  {
    "end": 8,
    "start": 0,
    "text": "John Doe",
    "type": "PERSON"
  },
  {
    "end": 25,
    "start": 13,
    "text": "Go Developer",
    "type": "POSITION"
  },
  {
    "end": 35,
    "start": 30,
    "text": "Google",
    "type": "ORG"
  },
]
```

## Usage

### Client Initialization

Pass the spaCy model you want to use and the NLP Cloud token to the client during initialization.

The spaCy model can either be a spaCy pretrained model like `en_core_web_sm`, `fr_core_news_lg`... but also one of your custom spaCy models using `custom_model/<model id>` (e.g. `custom_model/2568`).

Your token can be retrieved from your [NLP Cloud dashboard](https://nlpcloud.io/home/token).

```python
import nlpcloud

client = nlpcloud.Client("<model>", "<your token>")
```

### Entities Endpoint

Call the `entities()` method and pass the text you want to perform named entity recognition (NER) on.

```python
client.entities("<Your block of text>")
```

The above command returns a JSON object.


### Dependencies Endpoint

Call the `dependencies()` method and pass the text you want to perform part of speech tagging (POS) + arcs on.

```python
client.dependencies("<Your block of text>")
```

The above command returns a JSON object.

### Sentence Dependencies Endpoint

Call the `sentence_dependencies()` method and pass a block of text made up of several sentencies you want to perform POS + arcs on.

```python
client.sentence_dependencies("<Your block of text>")
```

The above command returns a JSON object.

### Library Versions Endpoint

Call the `lib_versions()` method to know the versions of the libraries used behind the hood with the model (for example the spaCy version used).

```python
client.lib_versions()
```

The above command returns a JSON object.

