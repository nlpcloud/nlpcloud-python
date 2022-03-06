from setuptools import setup

setup(
    name='nlpcloud',
    version='1.0.24',
    description='Python client for the NLP Cloud API',
    long_description="NLP Cloud serves high performance pre-trained or custom models for NER, sentiment-analysis, classification, summarization, paraphrasing, text generation, question answering, machine translation, language detection, semantic similarity, tokenization, POS tagging, embeddings, and dependency parsing. It is ready for production, served through a REST API.\n\nThis is the Python client for the API.\n\nMore details here: https://nlpcloud.io\n\nDocumentation: https://docs.nlpcloud.io\n\nGithub: https://github.com/nlpcloud/nlpcloud-python",
    packages=['nlpcloud'],
    author='Julien Salinas',
    author_email='all@juliensalinas.com',
    license='MIT',
    keywords=['api', 'NLP', 'spacy', 'Hugging Face', 'deep learning', 'machine learning',
              'data science', 'nlpcloud'],
    url='https://github.com/nlpcloud/nlpcloud-python',
    install_requires=['requests']
)
