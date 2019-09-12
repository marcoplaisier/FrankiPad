import random
import string

from forms import TextForm


def test_empty_app(client):
    rv = client.get('/')
    assert b"Create, update and send your texts to your display" in rv.data


def test_no_texts(client):
    rv = client.get('/index')
    assert b"No texts available." in rv.data


def test_add_text(client):
    text_id = 1
    ticker_text = "Test text"
    form = TextForm(ticker_text=ticker_text, active=True)
    rv = client.post('/text', data=form.data, follow_redirects=True)
    rv = client.get('/index')
    assert b"No texts available." not in rv.data


def test_get_text(client):
    text_id = 2
    text = "".join([random.choice(string.ascii_letters) for i in range(50)])
    form = TextForm(id=text_id, ticker_text=text, active=True)
    rv = client.post('/text', data=form.data, follow_redirects=True)
    rv = client.get(f'/text/{text_id}')
    assert bytes(text, 'utf-8') in rv.data


def test_edit_text(client):
    text_id = 3
    random_text = create_random_text()
    form = TextForm(id=text_id, ticker_text=random_text, active=True)
    rv = client.post('/text', data=form.data, follow_redirects=True)
    assert bytes(random_text, 'utf-8') in rv.data

    random_text = create_random_text()
    form = TextForm(id=text_id, ticker_text=random_text, active=True)
    client.post(f'/text/{text_id}', data=form.data, follow_redirects=True)
    rv = client.get(f'/text/{text_id}')
    assert bytes(random_text, 'utf-8') in rv.data


def create_random_text():
    return "".join([random.choice(string.ascii_letters) for i in range(50)])
