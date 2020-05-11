# -*- coding:utf-8 -*-
import sys
import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()
# 两边同时声明，防止另一方先启动，找不到该交换机报错
channel.exchange_declare(exchange="topic_msg", exchange_type="topic", durable=True)

res = channel.queue_declare(queue="", exclusive=True)
queue_name = res.method.queue
channel.queue_bind(queue=queue_name, exchange="topic_msg", routing_key='#.info.*')


def callback(ch, method, properties, body):
    print('start', time.asctime())
    print('[{}]: {}'.format(method.routing_key, body), properties)
    time.sleep(body.count(b'.'))
    print('end ', time.asctime())
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=False)
channel.start_consuming()
