#!/usr/bin/env python3
import pika
import time
from typing import List, Dict
import mysql.connector

import socket

pingcounter = 0
# isreachable = False
# while isreachable is False and pingcounter < 5:
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     try:
#         s.connect(('rabbitmq', 5672))
#         isreachable = True
#     except socket.error as e:
#         time.sleep(2)
#         pingcounter += 1
#     s.close()

# if isreachable:
print("Starting generating numbers")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
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
    val = ("3", "red")
    cursor.execute('INSERT INTO fibbonaci_numbers (number_id, title) VALUES ("3", "red")')
    cursor.close()
    connection.commit()
    connection.close()

channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()