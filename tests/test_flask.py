from app import app

import pytest


@pytest.fixture
def client():
    yield app.test_client()


def test_simple(client):
    t = client.get('/')
    assert b'Hello' in t.data
