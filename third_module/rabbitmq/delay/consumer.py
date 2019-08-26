# -*- coding:UTF-8 -*-
from third_module.rabbitmq.delay.client import RabbitMQClient


def callback(ch, method, properties, body):
    msg = body.decode()
    print(msg)
    # 如果处理成功，则调用此消息回复ack，表示消息成功处理完成。
    RabbitMQClient.message_handle_successfully(ch, method)


if __name__ == '__main__':
    print("start program")
    client = RabbitMQClient()
    queue_name = "RetryQueue"
    client.start_consume(callback, queue_name, delay=0)
