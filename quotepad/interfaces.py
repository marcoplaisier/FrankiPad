import os
import sqlite3
import time
from multiprocessing import Process
from unittest.mock import Mock

from quotepad.models import Text


try:
    import wiringpi
except ImportError:
    print('Wiringpi is missing')
    wiringpi = Mock()

from quotepad.serializers import BinaryTextEncoder

DATA_REQUEST_PIN = 4
CHANNEL = 0
SPEED = 25000

wiringpi.wiringPiSPISetup(CHANNEL, SPEED)
connection_string = "sqlite:///{}/quotepad.db".format(os.getcwd())
conn = sqlite3.connect(connection_string)
query = """select *
           from text
           where active = 1
           order by id asc"""
cursor = conn.cursor()
query_result = cursor.execute(query)
query_result = Text.query.all()


def send_data():
    global query_result

    try:
        data = next(query_result)
    except StopIteration:
        query_result = cursor.execute(query)
        data = next(query_result)

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
