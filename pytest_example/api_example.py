import requests

URL = 'https://reqres.in'


def login(email, password):
    path = '/api/login'
    data = {'email': email, 'password': password}
    return requests.get(URL + path, data)
