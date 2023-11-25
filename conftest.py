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
    token = requests.post(url=cfg['login'], data={'username': cfg['user'], 'password': cfg['pas']}).json()['token']
    print(token)
    return token