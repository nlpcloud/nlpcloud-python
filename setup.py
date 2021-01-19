from setuptools import setup

setup(
    name='nlpcloud',
    version='1.0.6',
    description='Python client for the NLP Cloud API',
    long_description="NLP Cloud serves all the spaCy pre-trained models, and your own custom models, through a RESTful API ready for production.\n\nThis is the Python client for the API.\n\nMore details here: https://nlpcloud.io\n\nDocumentation: https://docs.nlpcloud.io\n\nGithub: https://github.com/nlpcloud/nlpcloud-python",
    packages=['nlpcloud'],
    author='Julien Salinas',
    author_email='all@juliensalinas.com',
    license='MIT',
    keywords=['api', 'NLP', 'spacy', 'machine learning',
              'data science', 'nlpcloud'],
    url='https://github.com/nlpcloud/nlpcloud-python'
)
