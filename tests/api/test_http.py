import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(r.text)


@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunct')
    body = r.json()

    assert body['login'] == 'defunct'
    assert r.status_code == 200
    assert r.headers['Server'] == 'GitHub.com'


@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/sergii_butenko')
    assert r.status_code == 404
