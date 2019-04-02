import itertools
import os
import sqlite3
import time
from multiprocessing import Process

import wiringpi

DATA_REQUEST_PIN = 4
CHANNEL = 0
SPEED = 250000

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(DATA_REQUEST_PIN, wiringpi.GPIO.INPUT)
connection_string = f"sqlite:///{os.getcwd()}/quotepad.db"
conn = sqlite3.connect(connection_string)
query = """select *
           from text
           where active = TRUE
           order by id asc"""
cursor = conn.cursor()
query_result = cursor.execute(query)


def send_data():
    global query_result

    try:
        data = next(query_result)
    except StopIteration:
        query_result = cursor.execute(query)
        data = next(query_result)

    text = data.text
    text = itertools.zip_longest(text, [], fillvalue=0x07)
    text = list(itertools.chain.from_iterable(text))
    buffer = bytes(text, 'ascii')

    header = bytes([0xFE, 0x01, 0x00, 0x01, 0x00, 0x00])
    footer = bytes([0xFF])

    wiringpi.wiringPiSPIDataRW(0, header + buffer + footer)


def _run_process():
    wiringpi.wiringPiSPISetup(CHANNEL, SPEED)
    wiringpi.pinMode(DATA_REQUEST_PIN, wiringpi.GPIO.INPUT)
    wiringpi.wiringPiISR(DATA_REQUEST_PIN, wiringpi.GPIO.INT_EDGE_RISING, send_data)

    while True:
        time.sleep(0.1)


def run():
    Process(target=_run_process).start()
