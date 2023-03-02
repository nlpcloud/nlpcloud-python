from setuptools import setup

setup(
    name='nlpcloud',
    version='1.0.39',
    description='Python client for the NLP Cloud API',
    long_description="NLP Cloud serves high performance pre-trained or custom models for NER, sentiment-analysis, classification, summarization, paraphrasing, grammar and spelling correction, keywords and keyphrases extraction, chatbot, product description and ad generation, intent classification, text generation, image generation, blog post generation, code generation, question answering, automatic speech recognition, machine translation, language detection, semantic search, semantic similarity, tokenization, POS tagging, embeddings, and dependency parsing. It is ready for production, served through a REST API.\n\nThis is the Python client for the API.\n\nMore details here: https://nlpcloud.io\n\nDocumentation: https://docs.nlpcloud.io\n\nGithub: https://github.com/nlpcloud/nlpcloud-python",
    packages=['nlpcloud'],
    author='Julien Salinas',
    author_email='all@juliensalinas.com',
    license='MIT',
    keywords=['api', 'NLP', 'ai', 'deep learning', 'machine learning',
              'data science', 'nlpcloud'],
    url='https://github.com/nlpcloud/nlpcloud-python',
    install_requires=['requests']
)
