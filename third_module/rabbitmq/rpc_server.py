# -*- coding: utf-8 -*-
import pika
from pika.exceptions import AMQPError


class RpcServer(object):
    def __init__(self, queue_name="", prefetch_count=1):
        self.__connection_param = pika.ConnectionParameters(host="localhost", port=5672,
                                                            connection_attempts=10000, retry_delay=5)
        self.__connection = None
        self.__channel = None
        self.__prefetch_count = prefetch_count
        self.__queue_name = queue_name
        self._connect()

    def _connect(self):
        if not self.__connection or self.__connection.is_closed:
            self.__connection = pika.BlockingConnection(self.__connection_param)
            self.__channel = self.__connection.channel()
            self.__channel.queue_declare(queue=self.__queue_name)
            self.__channel.basic_qos(prefetch_count=self.__prefetch_count)
            self.__channel.basic_consume(queue=self.__queue_name, on_message_callback=self._on_request)

    def _on_request(self, ch, method, props, body):
        n = int(body)
        print(" [.] fib(%s)" % n)
        response = fib(n)

        ch.basic_publish(exchange='',
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(correlation_id=props.correlation_id),
                         body=str(response))
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def start(self):
        try:
            self.__channel.start_consuming()
        except AMQPError as e:
            print(e)
            self._connect()
            self.start()

    def close(self):
        if self.__connection and self.__connection.is_open:
            self.__connection.close()


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print("server start")
    rs = RpcServer(queue_name="rpc_queue")
    rs.start()
    rs.close()

