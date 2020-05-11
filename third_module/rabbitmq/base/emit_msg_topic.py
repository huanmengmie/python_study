# -*- coding:utf-8 -*-
import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = connection.channel()
channel.exchange_declare(exchange="topic_msg", exchange_type="topic", durable=True)

severity = sys.argv[1] if len(sys.argv) > 1 else 'info.test'
message = " ".join(sys.argv[2:])
print('[send message]: {}'.format(message))

channel.basic_publish(exchange="topic_msg", routing_key=severity, body=message,
                      properties=pika.BasicProperties(delivery_mode=2))

connection.close()

