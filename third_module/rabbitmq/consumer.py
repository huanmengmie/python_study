# !/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

import pika
from pika.exceptions import AMQPError


class RmqConsumer(object):
    def __init__(self, queue_name, process_func, prefetch_count=1, no_ack=True):
        """
        
        :param queue_name: 绑定到channel上的队列名称，可以多次调用，只生效一次
        :param process_func: 处理消息的方法名称
        :param prefetch_count: rmq默认轮循分配任务，设置prefetch_count=1时，正在执行任务的consumer不会分配task
        :param no_ack: 
        """
        self.__connection_param = pika.ConnectionParameters(host="localhost", port=5672,
                                                            connection_attempts=10000, retry_delay=5)
        self.__connection = None
        self.__channel = None
        self.__queue_name = queue_name
        self.__process_func = process_func
        self.__prefetch_count = prefetch_count
        self.__no_ack = no_ack
        self._connect()

    def _connect(self, reconnect=False):
        if not self.__connection or self.__connection.is_closed or reconnect:
            self.__connection = pika.BlockingConnection(self.__connection_param)
            self.__channel = self.__connection.channel()
            # 设置channel持久化
            self.__channel.queue_declare(queue=self.__queue_name, durable=True)
            self.__channel.basic_qos(prefetch_count=self.__prefetch_count)
            self.__channel.basic_consume(consumer_callback=self._on_message, queue=self.__queue_name,
                                         no_ack=self.__no_ack)

    def _on_message(self, ch, method, properties, body):
        print("ch => ", ch)
        print("method => ", method)
        print("properties => ", properties)
        print("body => ", body)
        if self.__process_func:
            self.__process_func(body, method.delivery_tag)

    def send_ack(self, delivery_tag):
        # 消息确认（设置no_ack=False时调用）
        if not self.__no_ack:
            self.__channel.basic_ack(delivery_tag=delivery_tag)

    def start(self):
        try:
            self.__channel.start_consuming()
        except socket.error as e:
            print(e)
            self._connect(True)
            self.start()


def test(body, delivery_tag):
    print("body => ", body)
    print("delivery_tag => ", delivery_tag)


if __name__ == '__main__':
    print("准备消费 ")
    rmc = RmqConsumer("hello", test)
    rmc.start()
