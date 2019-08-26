# -*- coding:UTF-8 -*-
from third_module.rabbitmq.delay.client import RabbitMQClient


def delay_queue():
    print("start program")
    client = RabbitMQClient()
    msg1 = '{"key":"value"}'
    client.publish_message('test-delay', msg1, delay=1, TTL=10000)
    print("message send out")


def delay_message():
    print("start program")
    client = RabbitMQClient()
    msg1 = '{"key":"value"}'
    client.publish_delay_message('test-message', "哈哈哈", delay=2000)
    client.publish_delay_message('test-message', msg1, delay=5000)
    client.publish_delay_message('test-message', "哈哈哈", delay=3000)
    client.close_connection()
    print("message send out")


if __name__ == '__main__':
    # delay_queue()
    delay_message()
