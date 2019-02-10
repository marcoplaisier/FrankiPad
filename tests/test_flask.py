from app import app

import pytest


@pytest.fixture
def client():
    yield app.test_client()


def test_simple(client):
    t = client.get('/')
    assert b'Setting your texts alight - Quotepad' in t.data
