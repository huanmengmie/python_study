# -*- coding: utf-8 -*-
import pika
from pika.exceptions import AMQPError


class RmqPublish(object):
    def __init__(self):
        self.__connection_param = pika.ConnectionParameters(host="192.168.153.129", port=5672,
                                                            connection_attempts=10000, retry_delay=5)
        self.__connection = None
        self.__channel = None
        self._connect()

    def _connect(self):
        if not self.__connection or self.__connection.is_closed:
            self.__connection = pika.BlockingConnection(self.__connection_param)
            self.__channel = self.__connection.channel()

    def _publish(self, msg, routing_key, delivery_mode, exchange_name):
        # delivery_mode = 2, 消息持久化
        self.__channel.basic_publish(exchange=exchange_name,
                                     routing_key=routing_key,
                                     body=msg,
                                     properties=pika.BasicProperties(delivery_mode=delivery_mode))

    def send(self, msg, routing_key, delivery_mode=2, exchange_name='', exchange_type='fanout'):
        try:
            self.__channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type)
            self._publish(msg, routing_key, delivery_mode, exchange_name)
        except AMQPError as e:
            print(e)
            self._connect()
            self.send(msg, routing_key, delivery_mode, exchange_name)

    def close(self):
        if self.__connection and self.__connection.is_open:
            self.__connection.close()


if __name__ == '__main__':
    print("开始生产")
    rmp = RmqPublish()
    for i in range(100):
        rmp.send("%d条信息" % i, routing_key="", exchange_type="log")
    rmp.close()
