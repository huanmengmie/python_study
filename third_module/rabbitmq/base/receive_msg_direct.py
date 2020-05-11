# -*- coding:utf-8 -*-
import sys
import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()
# 两边同时声明，防止另一方先启动，找不到该交换机报错
channel.exchange_declare(exchange="direct_msg", exchange_type="direct", durable=True)

res = channel.queue_declare(queue="", exclusive=True)
queue_name = res.method.queue

msg_types = sys.argv[1:]
if not msg_types:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for mt in msg_types:
    # 当采用direct类型的exchange,且生产者和消费者使用同一个exchange
    # 此处的routing_key与channel.publish#routing_key匹配时，消息会推到queue_name队列中
    channel.queue_bind(queue=queue_name, exchange="direct_msg", routing_key=mt)


def callback(ch, method, properties, body):
    print('start', time.asctime())
    print('[{}]: {}'.format(method.routing_key, body), properties)
    time.sleep(body.count(b'.'))
    print('end ', time.asctime())
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=False)
channel.start_consuming()