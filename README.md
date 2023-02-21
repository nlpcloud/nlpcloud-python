# Python Client For NLP Cloud

This is the Python client for the [NLP Cloud](https://nlpcloud.io) API. See the [documentation](https://docs.nlpcloud.io) for more details.

NLP Cloud serves high performance pre-trained or custom models for NER, sentiment-analysis, classification, summarization, dialogue summarization, paraphrasing, intent classification, product description and ad generation, chatbot, grammar and spelling correction, keywords and keyphrases extraction, text generation, image generation, blog post generation, source code generation, question answering, automatic speech recognition, machine translation, language detection, semantic search, semantic similarity, tokenization, POS tagging, embeddings, and dependency parsing. It is ready for production, served through a REST API.

You can either use the NLP Cloud pre-trained models, fine-tune your own models, or deploy your own models.

If you face an issue, don't hesitate to raise it as a Github issue. Thanks!

## Installation

Install via pip.

```shell
pip install nlpcloud
```

## Examples

Here is a full example that summarizes a text using Facebook's Bart Large CNN model, with a fake token:

```python
import nlpcloud

client = nlpcloud.Client("bart-large-cnn", "4eC39HqLyjWDarjtT1zdp7dc")
client.summarization("""One month after the United States began what has become a 
  troubled rollout of a national COVID vaccination campaign, the effort is finally 
  gathering real steam. Close to a million doses -- over 951,000, to be more exact -- 
  made their way into the arms of Americans in the past 24 hours, the U.S. Centers 
  for Disease Control and Prevention reported Wednesday. That s the largest number 
  of shots given in one day since the rollout began and a big jump from the 
  previous day, when just under 340,000 doses were given, CBS News reported. 
  That number is likely to jump quickly after the federal government on Tuesday 
  gave states the OK to vaccinate anyone over 65 and said it would release all 
  the doses of vaccine it has available for distribution. Meanwhile, a number 
  of states have now opened mass vaccination sites in an effort to get larger 
  numbers of people inoculated, CBS News reported.""")
```

Here is a full example that does the same thing, but on a GPU:

```python
import nlpcloud

client = nlpcloud.Client("bart-large-cnn", "4eC39HqLyjWDarjtT1zdp7dc", True)
client.summarization("""One month after the United States began what has become a 
  troubled rollout of a national COVID vaccination campaign, the effort is finally 
  gathering real steam. Close to a million doses -- over 951,000, to be more exact -- 
  made their way into the arms of Americans in the past 24 hours, the U.S. Centers 
  for Disease Control and Prevention reported Wednesday. That s the largest number 
  of shots given in one day since the rollout began and a big jump from the 
  previous day, when just under 340,000 doses were given, CBS News reported. 
  That number is likely to jump quickly after the federal government on Tuesday 
  gave states the OK to vaccinate anyone over 65 and said it would release all 
  the doses of vaccine it has available for distribution. Meanwhile, a number 
  of states have now opened mass vaccination sites in an effort to get larger 
  numbers of people inoculated, CBS News reported.""")
```

Here is a full example that does the same thing, but on a French text:

```python
import nlpcloud

client = nlpcloud.Client("bart-large-cnn", "4eC39HqLyjWDarjtT1zdp7dc", True, "fr")
client.summarization("""Sur des images aériennes, prises la veille par un vol de surveillance 
  de la Nouvelle-Zélande, la côte d’une île est bordée d’arbres passés du vert 
  au gris sous l’effet des retombées volcaniques. On y voit aussi des immeubles
  endommagés côtoyer des bâtiments intacts. « D’après le peu d’informations
  dont nous disposons, l’échelle de la dévastation pourrait être immense, 
  spécialement pour les îles les plus isolées », avait déclaré plus tôt 
  Katie Greenwood, de la Fédération internationale des sociétés de la Croix-Rouge.
  Selon l’Organisation mondiale de la santé (OMS), une centaine de maisons ont
  été endommagées, dont cinquante ont été détruites sur l’île principale de
  Tonga, Tongatapu. La police locale, citée par les autorités néo-zélandaises,
  a également fait état de deux morts, dont une Britannique âgée de 50 ans,
  Angela Glover, emportée par le tsunami après avoir essayé de sauver les chiens
  de son refuge, selon sa famille.""")
```

A json object is returned:

```json
{
  "summary_text": "Over 951,000 doses were given in the past 24 hours. That's the largest number of shots given in one day since the  rollout began. That number is likely to jump quickly after the federal government gave states the OK to vaccinate anyone over 65. A number of states have now opened mass vaccination sites."
}
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

If you want to make asynchronous requests, pass `asynchronous=True`.

```python
import nlpcloud

client = nlpcloud.Client("<model>", "<your token>", asynchronous=True)
```

If you are making asynchronous requests, you will always receive a quick response containing a URL. You should then poll this URL with `async_result()` on a regular basis (every 10 seconds for example) in order to check if the result is available. Here is an example:

```python
client.async_result("https://api.nlpcloud.io/v1/get-async-result/21718218-42e8-4be9-a67f-b7e18e03b436")
```

The above command returns a JSON object.

### Ad Generation And Product Description Endpoint

Call the `ad_generation()` method and pass a list of keywords you want to generate you product description or ad from.

```python
client.ad_generation(["Keyword 1", "Keyword 2", "Keyword 3", ...])
```

The above command returns a JSON object.

### Automatic Speech Recognition (Speech to Text) Endpoint

Call the `asr()` method and pass the following arguments:

1. (Optional: either this or the encoded file should be set) `url`: a URL where your audio or video file is hosted
1. (Optional: either this or the url should be set) `encoded_file`: a base 64 encoded version of your file
1. (Optional) `input_language`: the language of your file as ISO code

```python
client.asr("Your url")
```

The above command returns a JSON object.

### Blog Post Generation Endpoint

Call the `article_generation()` method and pass the title of your blog post:

```python
client.article_generation("<Your title>")
```

The above command returns a JSON object.

### Chatbot Endpoint

Call the `chatbot()` method and pass your input. As an option, you can also pass a context and conversation history that is a list of dictionnaries. Each dictionnary is made of an `input` and a `response` from the chatbot.

```python
client.chatbot("Your input", "You context", [{"input":"input 1","response":"response 1"}, {"input":"input 2","response":"response 2"}, ...])
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

### Code Generation Endpoint

Call the `code_generation()` method and pass the instruction for the program you want to generate:

```python
client.code_generation("<Your instruction>")
```

The above command returns a JSON object.

### Dependencies Endpoint

Call the `dependencies()` method and pass the text you want to perform part of speech tagging (POS) + arcs on.

```python
client.dependencies("<Your block of text>")
```

The above command returns a JSON object.

### Embeddings Endpoint

Call the `embeddings()` method and pass a list of blocks of text that you want to extract embeddings from.

```python
client.embeddings(["<Text 1>", "<Text 2>", "<Text 3>", ...])
```

The above command returns a JSON object.

### Entities Endpoint

Call the `entities()` method and pass the text you want to perform named entity recognition (NER) on.

```python
client.entities("<Your block of text>")
```

The above command returns a JSON object.

### Generation Endpoint

Call the `generation()` method and pass the following arguments:

1. The block of text that starts the generated text. 256 tokens maximum for GPT-J on CPU, 1024 tokens maximum for GPT-J and GPT-NeoX 20B on GPU, and 2048 tokens maximum for Fast GPT-J and Finetuned GPT-NeoX 20B on GPU.
1. (Optional) `min_length`: The minimum number of tokens that the generated text should contain. 256 tokens maximum for GPT-J on CPU, 1024 tokens maximum for GPT-J and GPT-NeoX 20B on GPU, and 2048 tokens maximum for Fast GPT-J and Finetuned GPT-NeoX 20B on GPU.. If `length_no_input` is false, the size of the generated text is the difference between `min_length` and the length of your input text. If `length_no_input` is true, the size of the generated text simply is `min_length`. Defaults to 10.
1. (Optional) `max_length`: Optional. The maximum number of tokens that the generated text should contain. 256 tokens maximum for GPT-J on CPU, 1024 tokens maximum for GPT-J and GPT-NeoX 20B on GPU, and 2048 tokens maximum for Fast GPT-J and Finetuned GPT-NeoX 20B on GPU. If `length_no_input` is false, the size of the generated text is the difference between `max_length` and the length of your input text. If `length_no_input` is true, the size of the generated text simply is `max_length`. Defaults to 50.
1. (Optional) `length_no_input`: Whether `min_length` and `max_length` should not include the length of the input text, as a boolean. If false, `min_length` and `max_length` include the length of the input text. If true, min_length and `max_length` don't include the length of the input text. Defaults to false.
1. (Optional) `end_sequence`: A specific token that should be the end of the generated sequence, as a string. For example if could be `.` or `\n` or `###` or anything else below 10 characters.
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
1. (Optional) `remove_end_sequence`: Optional. Whether you want to remove the `end_sequence` string from the result. Defaults to false.

```python
client.generation("<Your input text>")
```

The above command returns a JSON object.

### Grammar and Spelling Correction Endpoint

Call the `gs_correction()` method and pass the text you want correct:

```python
client.gs_correction("<Your block of text>")
```

The above command returns a JSON object.

### Image Generation Endpoint

Call the `image_generation()` method and pass the text instruction for the new image you want to generate:

```python
client.image_generation("<Your block of text>")
```

The above command returns a JSON object.

### Intent Classification Endpoint

Call the `intent_classification()` method and pass the text you want to extract intents from:

```python
client.intent_classification("<Your block of text>")
```

The above command returns a JSON object.

### Keywords and Keyphrases Extraction Endpoint

Call the `kw_kp_extraction()` method and pass the text you want to extract keywords and keyphrases from:

```python
client.kw_kp_extraction("<Your block of text>")
```

The above command returns a JSON object.

### Language Detection Endpoint

Call the `langdetection()` method and pass the text you want to analyze in order to detect the languages.

```python
client.langdetection("<The text you want to analyze>")
```

The above command returns a JSON object.

### Library Versions Endpoint

Call the `lib_versions()` method to know the versions of the libraries used behind the hood with the model (for example the PyTorch, TensorFlow, or spaCy version used).

```python
client.lib_versions()
```

The above command returns a JSON object.

### Paraphrasing Endpoint

Call the `paraphrasing()` method and pass the text you want to paraphrase.

```python
client.paraphrasing("<Your text to paraphrase>")
```

The above command returns a JSON object.

### Question Answering Endpoint

Call the `question()` method and pass the following:

1. A context that the model will use to try to answer your question
1. Your question

```python
client.question("<Your question>", "<Your context>")
```

The above command returns a JSON object.

### Semantic Search Endpoint

Call the `semantic_search()` method and pass a your search query.

```python
client.semantic_search("Your search query")
```

The above command returns a JSON object.

### Semantic Similarity Endpoint

Call the `semantic_similarity()` method and pass a list made up of 2 blocks of text that you want to compare.

```python
client.semantic_similarity(["<Block of text 1>", "<Block of text 2>"])
```

The above command returns a JSON object.

### Sentence Dependencies Endpoint

Call the `sentence_dependencies()` method and pass a block of text made up of several sentences you want to perform POS + arcs on.

```python
client.sentence_dependencies("<Your block of text>")
```

The above command returns a JSON object.

### Sentiment Analysis Endpoint

Call the `sentiment()` method and pass the text you want to analyze the sentiment of:

```python
client.sentiment("<Your block of text>")
```

The above command returns a JSON object.

### Summarization Endpoint

Call the `summarization()` method and pass the text you want to summarize.

```python
client.summarization("<Your text to summarize>")
```

The above command returns a JSON object.

### Tokenization Endpoint

Call the `tokens()` method and pass the text you want to tokenize.

```python
client.tokens("<Your block of text>")
```

The above command returns a JSON object.

### Translation Endpoint

Call the `translation()` method and pass the text you want to translate.

```python
client.translation("<Your text to translate>")
```

The above command returns a JSON object.
