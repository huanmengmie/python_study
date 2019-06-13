# -*- coding: utf-8 -*-

"""
    exchange type:
                fanout（群发）: 扇形，无脑群发
                direct（选择）: 根据routing key 进行匹配，发给匹配的subscribe
                topic（主题）： 将routing_key与消息内容匹配
                            * 表示一个字符       # 表示0或多个字符
                            单用#时，相当于订阅所有队列，与fanout类型相似
                            * 和 # 都不用时，指定key ，与direct类型相似

"""
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


def pub_fanout():
    print("开始生产")
    rmp = RmqPublish()
    for i in range(100):
        rmp.send("%d条信息" % i, routing_key="", exchange_name="log")
    rmp.close()


def pub_direct(routing_key, msg):
    print("开始生产")
    rmp = RmqPublish()
    for i in range(100):
        rmp.send("%d条信息%s" % (i, msg), routing_key=routing_key, exchange_name="direct_log", exchange_type="direct")
    rmp.close()


def pub_topic(routing_key, msg):
    print("开始生产")
    rmp = RmqPublish()
    for i in range(100):
        rmp.send("%d条信息%s" % (i, msg), routing_key=routing_key, exchange_name="topic_log", exchange_type="topic")
    rmp.close()

if __name__ == '__main__':
    # pub_fanout()

    # pub_direct("a", "哈哈哈")
    # pub_direct("b", "吼吼吼")

    pub_topic("a.b.c", "啊啊啊啊")
    pub_topic("hello.b", "呃呃呃")
