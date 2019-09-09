import os
import sqlite3
import time
from multiprocessing import Process
from unittest.mock import Mock

from models import Text
from serializers import BinaryTextEncoder

try:
    import wiringpi
except ImportError:
    print('Wiringpi is missing')
    wiringpi = Mock()

DATA_REQUEST_PIN = 4
CHANNEL = 0
SPEED = 25000

wiringpi.wiringPiSPISetup(CHANNEL, SPEED)




def send_data():
    try:
        last_text_sent = Text.query.filter(last_sent=True).first()
        text_to_send = Text.q

    bytes_to_send = BinaryTextEncoder.serialize(data)
    wiringpi.wiringPiSPIDataRW(0, bytes_to_send)


def reset():
    global query_result
    query_result = cursor.execute(query)


def _run_process():
    while True:
        send_data()
        time.sleep(10)


def run():
    Process(target=_run_process).start()
