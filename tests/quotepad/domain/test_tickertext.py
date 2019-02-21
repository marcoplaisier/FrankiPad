import uuid

from quotepad.domain.tickertext import TickerText


def test_tickertext_init():
    id = uuid.uuid4()
    text = 'This is a test text'
    active = True

    tt = TickerText(id, text, active)
    assert tt.id == id
    assert tt.text == text
    assert tt.active == active


def test_tickertext_from_dict():
    id = uuid.uuid4()

    tt = TickerText.from_dict({
        'id': id,
        'text': 'This is a test text',
        'active': True
    })
    assert tt.id == id
    assert tt.text == 'This is a test text'
    assert tt.active == True
