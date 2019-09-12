import pytest

from models import Text


@pytest.mark.skip(reason="Work in progress")
def test_send_data():
    active_texts = Text.query.filter_by(active=True).all()
    for active_text in active_texts:
        print(active_text)
    pytest.fail(msg="Failing...")
