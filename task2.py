'''Написать тест с использованием pytest и requests, в котором:

Адрес сайта, имя пользователя и пароль хранятся в config.yaml

conftest.py содержит фикстуру авторизации по адресу https://test-stand.gb.ru/gateway/login с передачей параметров “username" и "password"
и возвращающей токен авторизации

Тест с использованием DDT проверяет наличие поста
с определенным заголовком в списке постов другого пользователя, для этого выполняется get запрос
по адресу https://test-stand.gb.ru/api/posts c хедером, содержащим токен авторизации в параметре "X-Auth-Token".
Для отображения постов другого пользователя передается "owner": "notMe".

http://restapi.adequateshop.com/api/authaccount/registration

http://restapi.adequateshop.com/api/authaccount/login'''


import requests
import yaml

with open('config.yaml', encoding='utf-8') as f:
    cfg = yaml.safe_load(f)


def test_1(token = requests.post(url=cfg['login'], data={'username': cfg['user'], 'password': cfg['pas']}).json()['token']):
    desc = cfg['post_desc']
    print(desc)
    res_get = requests.get(url=cfg['posts'], headers={'X-Auth-Token': token}, params={'owner': 'notMe'}).json()
    # print(res_get)
    res = False
    for post in res_get['data']:
        if desc in post['description']:
            res = True
    assert res, 'POST NOT FOUND'



