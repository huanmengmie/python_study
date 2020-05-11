# -*- coding:utf-8 -*-
import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = connection.channel()
channel.exchange_declare(exchange="direct_msg", exchange_type="direct", durable=True)

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = " ".join(sys.argv[2:])
print('[send message]: {}'.format(message))

channel.basic_publish(exchange="direct_msg", routing_key=severity, body=message,
                      properties=pika.BasicProperties(delivery_mode=2))

connection.close()

