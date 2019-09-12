from models import Text


def test_simple_text(session):
    t = Text(text='test text', active=True)
    session.add(t)
    session.commit()

    assert t.id > 0


def test_two_texts(session):
    t1 = Text(text='text1', active=True)
    t2 = Text(text='text2', active=True)
    session.add(t1)
    session.add(t2)
    session.commit()

    assert t1.id > 0
    assert t2.id > 0
