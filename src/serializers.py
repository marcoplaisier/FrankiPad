import itertools

import models

HEADER = bytes([0xFE, 0x01, 0x00, 0x01, 0x00, 0x00])
FOOTER = bytes([0xFF])
FOREGROUND_COLORS = {
    'blue': 0x01,
    'green': 0x02,
    'red': 0x03,
    'cyan': 0x04,
    'magenta': 0x05,
    'yellow': 0x06,
    'white': 0x07,
}


class BinaryTextEncoder:

    @staticmethod
    def serialize(text: models.Text):
        text = bytes(text.text, 'ascii')
        text_with_colors = itertools.zip_longest(text, [], fillvalue=FOREGROUND_COLORS['blue'])
        text_bytes = bytes(itertools.chain.from_iterable(text_with_colors))

        return HEADER + text_bytes + FOOTER
