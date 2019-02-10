from app import app

import pytest


@pytest.fixture
def client():
    yield app.test_client()


def test_simple(client):
    t = client.get('/')
    assert b'Setting your texts alight - Quotepad' in t.data
    assert b'/text' in t.data
    assert b'/index' in t.data


def test_list_page(client):
    page = client.get('/text')
    assert b'Save' in page.data
    assert b'<textarea' in page.data
