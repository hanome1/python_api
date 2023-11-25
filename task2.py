import requests
import yaml

with open('config.yaml') as f:
    cfg = yaml.safe_load(f)

token = requests.post(url=cfg['login'], data={'username': cfg['user'], 'password': cfg['pas']}).json()['token']
# print(token)
get = requests.get(url=cfg['posts'], headers={'X-Auth-Token': token}, params={'owner': 'notMe'}).json()
print(get)