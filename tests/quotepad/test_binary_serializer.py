from datetime import datetime

import pytest

from models import Text
from serializers import HEADER, FOOTER, BinaryTextEncoder


def test_no_text():
    test_text = Text(text="")
    expected_binary = bytes(HEADER + FOOTER)
    observed_binary = BinaryTextEncoder.serialize(test_text)

    assert observed_binary == expected_binary


def test_single_letter():
    text = "a"
    test_text = Text(text=text)
    expected_binary = HEADER + bytes(text, 'ascii') + bytes([0x01]) + FOOTER
    observed_binary = BinaryTextEncoder.serialize(test_text)

    assert observed_binary == expected_binary


def test_longer_text():
    text = "test"
    test_text = Text(text=text)
    expected_binary = HEADER + bytes.fromhex('74 01 65 01 73 01 74 01') + FOOTER
    observed_binary = BinaryTextEncoder.serialize(test_text)

    assert observed_binary == expected_binary


def test_unicode():
    text = "€"
    test_text = Text(text=text, active=True, created=datetime.now())
    with pytest.raises(UnicodeEncodeError, match=r".* ordinal not in range.*"):
        BinaryTextEncoder.serialize(test_text)
