# -*- coding: utf-8 -*-
import socket
import uuid

import pika


class RpcClient(object):
    def __init__(self, queue_name, prefetch_count=1, no_ack=True):
        self.__connection_param = pika.ConnectionParameters(host="localhost", port=5672,
                                                            connection_attempts=10000, retry_delay=5)
        self.__connection = None
        self.__channel = None
        self.__response = None
        self.__corr_id = None
        self.__callback_queue = None
        self.__queue_name = queue_name
        self.__prefetch_count = prefetch_count
        self.__no_ack = no_ack
        self._connect()

    def _connect(self, reconnect=False):
        if not self.__connection or self.__connection.is_closed or reconnect:
            self.__connection = pika.BlockingConnection(self.__connection_param)
            self.__channel = self.__connection.channel()
            # exclusive=True当消费者被销毁，queue队列也应该被销毁
            # result 为随机名称的queue
            result = self.__channel.queue_declare(exclusive=True)
            self.__callback_queue = result.method.queue

            self.__channel.basic_consume(consumer_callback=self._on_response, queue=self.__callback_queue,
                                         no_ack=self.__no_ack)

    def _on_response(self, ch, method, properties, body):
        if properties.correlation_id == self.__corr_id:
            self.__response = body
            print("%s" % body.decode("utf-8"))

    def call(self, n):
        self.__corr_id = str(uuid.uuid4())
        self.__channel.basic_publish(
            exchange='',
            routing_key=self.__queue_name,
            properties=pika.BasicProperties(
                reply_to=self.__callback_queue,
                correlation_id=self.__corr_id,
            ),
            body=str(n))
        while self.__response is None:
            self.__connection.process_data_events()
        return int(self.__response)


if __name__ == '__main__':
    print("client start")
    rc = RpcClient("rpc_queue")
    result = rc.call(5)
    print(result)
