# -*- coding: utf-8 -*-
import socket
import uuid

import pika


class RpcClient(object):
    def __init__(self, queue_name, prefetch_count=1, auto_ack=True):
        self.__connection_param = pika.ConnectionParameters(host="localhost", port=5672,
                                                            connection_attempts=10000, retry_delay=5)
        self.__connection = None
        self.__channel = None
        self.__response = None
        self.__corr_id = None
        # 接收sever端返回处理结果的队列
        self.__callback_queue = None
        self.__queue_name = queue_name
        self.__prefetch_count = prefetch_count
        self.__auto_ack = auto_ack
        self._connect()

    def _connect(self, reconnect=False):
        if not self.__connection or self.__connection.is_closed or reconnect:
            self.__connection = pika.BlockingConnection(self.__connection_param)
            self.__channel = self.__connection.channel()
            # exclusive=True当消费者被销毁，queue队列也应该被销毁
            # result 为随机名称的queue
            gen_queue = self.__channel.queue_declare(exclusive=True, queue="")
            self.__callback_queue = gen_queue.method.queue

            self.__channel.basic_consume(on_message_callback=self._on_response, queue=self.__callback_queue,
                                         auto_ack=self.__auto_ack)

    def _on_response(self, ch, method, properties, body):
        if properties.correlation_id == self.__corr_id:
            self.__response = body
            print("%s" % body.decode("utf-8"))

    def call(self, n):
        # 每个客户端维护一个处理请求结果的队列。为了分辨返回结果是否是当前请求，需要在数据传输过程中带入一个唯一的correlation_id
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
            # 确保数据被处理
            self.__connection.process_data_events()
        return int(self.__response)


if __name__ == '__main__':
    print("client start")
    rc = RpcClient("rpc_queue")
    result = rc.call(30)
    print(result)
