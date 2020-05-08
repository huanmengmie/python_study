# -*- coding:utf-8 -*-
import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    # 消息处理完成后的确认标志
    ch.basic_ack(delivery_tag=method.delivery_tag)


# 公平调度，当前消费者任务未完成时，不会分配新任务
channel.basic_qos(prefetch_count=1)
# callback收到消息后的回调
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()
