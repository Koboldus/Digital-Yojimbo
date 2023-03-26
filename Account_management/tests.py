import pytest
from django.test import TestCase, Client

from config import settings


def client():
    client = Client()
    return client


def test_main_logging_in(db, client):
    response = client.post('', {'username': 'test', 'password': '123'})
    assert response.status_code == 200


def test_main_get(client):
    response = client.get('')
    assert response.status_code == 200


def test_register_get(client):
    response = client.get('')
    assert response.status_code == 200


def test_register_failure(db, client):
    response = client.post('/register/', {
        'first_name': 'Adam',
        'last_name': 'Janczak',
        'email': 't@est.com',
        'username': 'meme',
        'password': 'bazinga',
        'password_repeat': 'bezinga',
    })
    assert response.status_code == 200


def test_logged_in_get(client):
    response = client.get('/account/')
    assert response.status_code == 302


def test_logged_in_post(client):
    c = client.post('/account/')
    assert c.status_code == 302


def test_account_delete_get(client):
    c = client.get('/account/delete/')
    assert c.status_code == 302


def test_account_delete_post(db, client):
    c = client.post('/account/delete/', {
        'username': 'test',
        'mail': 'b@b.com',
        'password': '123',
    })
    assert c.status_code == 200
