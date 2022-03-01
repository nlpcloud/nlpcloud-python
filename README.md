# Python Client For NLP Cloud

This is the Python client for the [NLP Cloud](https://nlpcloud.io) API. See the [documentation](https://docs.nlpcloud.io) for more details.

NLP Cloud serves high performance pre-trained for NER, sentiment-analysis, classification, summarization, text generation, question answering, machine translation, language detection, tokenization, lemmatization, POS tagging, and dependency parsing. It is ready for production, served through a REST API.

You can either use the NLP Cloud pre-trained models, fine-tune your own models, or deploy your own models.

If you face an issue, don't hesitate to raise it as a Github issue. Thanks!

## Installation

Install via pip.

```shell
pip install nlpcloud
```

## Examples

Here is a full example that performs Named Entity Recognition (NER) using spaCy's `en_core_web_lg` model, with a fake token:

```python
import nlpcloud

client = nlpcloud.Client("en_core_web_lg", "4eC39HqLyjWDarjtT1zdp7dc")
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

Pass the model you want to use and the NLP Cloud token to the client during initialization.

The model can either be a pretrained model like `en_core_web_lg`, `bart-large-mnli`... but also one of your custom models, using `custom_model/<model id>` (e.g. `custom_model/2568`). See the documentation for a [comprehensive list of all the models available](https://docs.nlpcloud.io/#models-list).

Your token can be retrieved from your [NLP Cloud dashboard](https://nlpcloud.io/home/token).

```python
import nlpcloud

client = nlpcloud.Client("<model>", "<your token>")
```

If you want to use a GPU, pass `gpu=True`.

```python
import nlpcloud

client = nlpcloud.Client("<model>", "<your token>", gpu=True)
```

If you want to use the multilingual add-on in order to process non-English texts, pass `lang="<your language code>"`. For example, if you want to process French text, you should set `lang="fr"`.

```python
import nlpcloud

client = nlpcloud.Client("<model>", "<your token>", lang="<your language code>")
```

### Entities Endpoint

Call the `entities()` method and pass the text you want to perform named entity recognition (NER) on.

```python
client.entities("<Your block of text>")
```

The above command returns a JSON object.

### Classification Endpoint

Call the `classification()` method and pass the following arguments:

1. The text you want to classify, as a string
1. The candidate labels for your text, as a list of strings
1. (Optional) `multi_class`: Whether the classification should be multi-class or not, as a boolean. Defaults to true.

```python
client.classification("<Your block of text>", ["label 1", "label 2", "..."])
```

The above command returns a JSON object.

### Text Generation Endpoint

Call the `generation()` method and pass the following arguments:

1. The block of text that starts the generated text, as a string. 1200 tokens maximum.
1. (Optional) `min_length`: The minimum number of tokens that the generated text should contain, as an integer. The size of the generated text should not exceed 256 tokens on a CPU plan and 1024 tokens on GPU plan. If `length_no_input` is false, the size of the generated text is the difference between `min_length` and the length of your input text. If `length_no_input` is true, the size of the generated text simply is `min_length`. Defaults to 10.
1. (Optional) `max_length`: The maximum number of tokens that the generated text should contain, as an integer. The size of the generated text should not exceed 256 tokens on a CPU plan and 1024 tokens on GPU plan. If `length_no_input` is false, the size of the generated text is the difference between `max_length` and the length of your input text. If `length_no_input` is true, the size of the generated text simply is `max_length`. Defaults to 50.
1. (Optional) `length_no_input`: Whether `min_length` and `max_length` should not include the length of the input text, as a boolean. If false, `min_length` and `max_length` include the length of the input text. If true, min_length and `max_length` don't include the length of the input text. Defaults to false.
1. (Optional) `end_sequence`: A specific token that should be the end of the generated sequence, as a string. For example if could be `.` or `\n` or `###` or anything else below 10 characters.
1. (Optional) `remove_end_input`: Whether you want to remove the end sequence form the result, as a boolean. Defaults to false.
1. (Optional) `remove_input`: Whether you want to remove the input text form the result, as a boolean. Defaults to false.
1. (Optional) `do_sample`: Whether or not to use sampling ; use greedy decoding otherwise, as a boolean. Defaults to true.
1. (Optional) `num_beams`: Number of beams for beam search. 1 means no beam search. This is an integer. Defaults to 1.
1. (Optional) `early_stopping`: Whether to stop the beam search when at least num_beams sentences are finished per batch or not, as a boolean. Defaults to false.
1. (Optional) `no_repeat_ngram_size`: If set to int > 0, all ngrams of that size can only occur once. This is an integer. Defaults to 0.
1. (Optional) `num_return_sequences`: The number of independently computed returned sequences for each element in the batch, as an integer. Defaults to 1.
1. (Optional) `top_k`: The number of highest probability vocabulary tokens to keep for top-k-filtering, as an integer. Maximum 1000 tokens. Defaults to 0.
1. (Optional) `top_p`: If set to float < 1, only the most probable tokens with probabilities that add up to top_p or higher are kept for generation. This is a float. Should be between 0 and 1. Defaults to 0.7.
1. (Optional) `temperature`: The value used to module the next token probabilities, as a float. Should be between 0 and 1. Defaults to 1.
1. (Optional) `repetition_penalty`: The parameter for repetition penalty, as a float. 1.0 means no penalty. Defaults to 1.0.
1. (Optional) `length_penalty`: Exponential penalty to the length, as a float. 1.0 means no penalty. Set to values < 1.0 in order to encourage the model to generate shorter sequences, or to a value > 1.0 in order to encourage the model to produce longer sequences. Defaults to 1.0.
1. (Optional) `bad_words`: List of tokens that are not allowed to be generated, as a list of strings. Defaults to null.

```python
client.generation("<Your input text>")
```

The above command returns a JSON object.

### Sentiment Analysis Endpoint

Call the `sentiment()` method and pass the text you want to analyze the sentiment of:

```python
client.sentiment("<Your block of text>")
```

The above command returns a JSON object.

### Question Answering Endpoint

Call the `question()` method and pass the following:

1. A context that the model will use to try to answer your question
1. Your question

```python
client.question("<Your context>", "<Your question>")
```

The above command returns a JSON object.

### Summarization Endpoint

Call the `summarization()` method and pass the text you want to summarize.Remo

```python
client.summarization("<Your text to summarize>")
```

The above command returns a JSON object.

### Translation Endpoint

Call the `translation()` method and pass the text you want to translate.

```python
client.translation("<Your text to translate>")
```

The above command returns a JSON object.

### Language Detection Endpoint

Call the `langdetection()` method and pass the text you want to analyze in order to detect the languages.

```python
client.langdetection("<The text you want to analyze>")
```

The above command returns a JSON object.

### Semantic Similarity Endpoint

Call the `semantic_similarity()` method and pass a list made up of 2 blocks of text that you want to compare.

```python
client.semantic_similarity(["<Block of text 1>", "<Block of text 2>"])
```

The above command returns a JSON object.

### Tokenization Endpoint

Call the `tokens()` method and pass the text you want to tokenize.

```python
client.tokens("<Your block of text>")
```

The above command returns a JSON object.

### Dependencies Endpoint

Call the `dependencies()` method and pass the text you want to perform part of speech tagging (POS) + arcs on.

```python
client.dependencies("<Your block of text>")
```

The above command returns a JSON object.

### Sentence Dependencies Endpoint

Call the `sentence_dependencies()` method and pass a block of text made up of several sentences you want to perform POS + arcs on.

```python
client.sentence_dependencies("<Your block of text>")
```

The above command returns a JSON object.

### Embeddings Endpoint

Call the `embeddings()` method and pass a list of blocks of text that you want to extract embeddings from.

```python
client.embeddings(["<Text 1>", "<Text 2>", "<Text 3>", ...])
```

The above command returns a JSON object.

### Library Versions Endpoint

Call the `lib_versions()` method to know the versions of the libraries used behind the hood with the model (for example the PyTorch, TensorFlow, or spaCy version used).

```python
client.lib_versions()
```

The above command returns a JSON object.
