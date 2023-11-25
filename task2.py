'''
Написать тест с использованием pytest и requests, в котором:
Адрес сайта, имя пользователя и пароль хранятся в config.yaml
conftest.py содержит фикстуру авторизации по адресу https://test-stand.gb.ru/gateway/login с передачей параметров “username" и "password"
и возвращающей токен авторизации
Тест с использованием DDT проверяет наличие поста
с определенным заголовком в списке постов другого пользователя, для этого выполняется get запрос
по адресу https://test-stand.gb.ru/api/posts c хедером, содержащим токен авторизации в параметре "X-Auth-Token".
Для отображения постов другого пользователя передается "owner": "notMe".
'''


import requests
import yaml

with open('config.yaml', encoding='utf-8') as f:
    cfg = yaml.safe_load(f)


def test_1(token):
    res_get = requests.get(url=cfg['posts'], headers={'X-Auth-Token': token}, params={'owner': 'notMe'}).json()
    print(res_get)
    res = False
    for post in res_get['data']:
        if cfg['post_desc'] in post['description']:
            res = True
    assert res, 'POST NOT FOUND'


'''
Добавить в задание с REST API ещё один тест, в котором создаётся новый пост, а потом проверяется его наличие на сервере по полю «описание».
Подсказка: создание поста выполняется запросом к https://test-stand.gb.ru/api/posts с передачей параметров title, description, content.
'''
def test_2(token):
    post = requests.post(url=cfg['posts'], headers={'X-Auth-Token': token}, params={'title': 'Test title', 'description': cfg['post_test_desc'], 'content': 'test text content\n'*10})
    res_get = requests.get(url=cfg['posts'], headers={'X-Auth-Token': token}, params={'description': cfg['post_test_desc']}).json()
    res = False
    for post in res_get['data']:
        if cfg['post_test_desc'] == post['description']:
            res = True
    assert res, 'POST NOT FOUND'

