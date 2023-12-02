import pytest
import requests
import yaml
from module import Site

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


# seminar2

@pytest.fixture()
def login_field():
    return """//*[@id="login"]/div[1]/label/input"""

@pytest.fixture()
def pas_field():
    return """//*[@id="login"]/div[2]/label/input"""

@pytest.fixture()
def btn():
    return """//*[@id="login"]/div[3]/button"""

@pytest.fixture()
def err_label():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""

@pytest.fixture()
def site():
    site = Site(cfg["address"])
    yield site
    site.close()