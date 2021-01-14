from setuptools import setup

setup(
    name='spacycloud',
    version='1.0.3',
    description='Python client for the spaCy Cloud API',
    long_description="spaCy Cloud serves all the spaCy pre-trained models, and your own custom models, through a RESTful API ready for production.\n\nThis is the Python client for the API.\n\nMore details here: https://spacycloud.io\n\nDocumentation: https://docs.spacycloud.io\n\nGithub: https://github.com/spacycloud/spacycloud-python",
    packages=['spacycloud'],
    author='Julien Salinas',
    author_email='all@juliensalinas.com',
    license='MIT',
    keywords=['api', 'NLP', 'spacy', 'machine learning',
              'data science', 'spacycloud'],
    url='https://github.com/spacycloud/spacycloud-python'
)
