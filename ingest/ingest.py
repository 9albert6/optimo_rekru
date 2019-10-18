#!/usr/bin/env python3
import pika
import time
from typing import List, Dict
import mysql.connector

import socket

def is_rabbitmq_reachable() -> bool:
    pingcounter = 0
    isreachable_rabbitmq = False
    while isreachable_rabbitmq is False and pingcounter < 5:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(('rabbitmq', 5672))
            isreachable_rabbitmq = True
        except socket.error:
            time.sleep(2)
            pingcounter += 1
        s.close()

    return isreachable_rabbitmq


def is_database_reachable() -> bool:
    pingcounter2 = 0
    isreachable_db = False
    while isreachable_db is False and pingcounter2 < 5:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(('database', 3306))
            isreachable_db = True
        except socket.error:
            time.sleep(2)
            pingcounter2 += 1
        s.close()

    return isreachable_db


def callback(ch: str, method: str, properties: str, body: str) -> None:
    n = int(body)
    print(" [x] Received %r" % body)
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'database',
        'port': '3306',
        'database': 'fibbonaci'
    }   
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO fibbonaci_numbers (fib_number) VALUE (%s);""" % (n))
    connection.commit()
    connection.close()


def connect_and_consume() -> None:
    if is_rabbitmq_reachable() and is_database_reachable():
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbitmq'))
        channel = connection.channel()

        channel.queue_declare(queue='fibbonaci')

        channel.basic_consume(
            queue='fibbonaci', on_message_callback=callback, auto_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()


if __name__== "__main__":
    connect_and_consume()