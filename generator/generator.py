#!/usr/bin/env python3
import pika
import time
import socket

#postpone connection to RabbitMq in order to avoid errors and restarting service
def is_rabbitmq_reachable():
    pingcounter = 0
    isreachable = False

    while isreachable is False and pingcounter < 5:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(('rabbitmq', 5672))
            isreachable = True
        except socket.error:
            time.sleep(10)
            pingcounter += 1
        s.close()

    return isreachable


def fib_generator(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_generator(n - 1) + fib_generator(n - 2)


def connect_and_generate():
    if is_rabbitmq_reachable():
        print("Starting generating numbers")
        connection = pika.BlockingConnection(
           pika.ConnectionParameters(host='rabbitmq'))
        channel = connection.channel()

        channel.queue_declare(queue='fibbonaci')

        n = 0
        while True:
            value = fib_generator(n)
            channel.basic_publish(exchange='', routing_key='fibbonaci', body=str(value))
            print(" [x] Fibbonaci number generated'")
            time.sleep(2)
            n += 1
        connection.close()


if __name__== "__main__":
    connect_and_generate()