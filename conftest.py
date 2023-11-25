import pytest
import requests
import yaml

with open('config.yaml') as f:
    cfg = yaml.safe_load(f)

@pytest.fixture()
def word_good():
    return 'колбаса'

@pytest.fixture()
def word_bad():
    return 'калбаса'

@pytest.fixture()
def token():
    return requests.post(url=cfg['login'], data={'username': cfg['user'], 'password': cfg['pas']}).json()['token']

@pytest.fixture()
def post_create():
    res = requests.post(url=cfg['posts'], headers={'X-Auth-Token': token}, params={'title': 'Test title', 'description': cfg['post_test_desc'], 'content': 'test text content\n'*10})
