# -*- coding:utf-8 -*-
import sys

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = connection.channel()
channel.exchange_declare(exchange="msgs", exchange_type="fanout", durable=True)

message = " ".join(sys.argv[1:]) or 'hello world...'
channel.basic_publish(exchange="msgs", routing_key="", body=message,
                      properties=pika.BasicProperties(delivery_mode=2))

connection.close()

