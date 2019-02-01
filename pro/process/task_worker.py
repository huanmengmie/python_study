# -*- coding:UTF-8 -*-
import time
from multiprocessing.managers import BaseManager
from queue import Queue


class QueueManger(BaseManager):
    pass


QueueManger.register("get_task_queue")
QueueManger.register("get_result_queue")

print("尝试连接主进程")
sever_address = "127.0.0.1"
m = QueueManger(address=(sever_address, 5000), authkey=b'123456')
m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

for x in range(10):
    try:
        n = task.get(timeout=10)
        print("执行 %d * %d" % (n, n))
        time.sleep(1)
        result.put("%d * %d = %d" % (n, n, n * n))
    except Queue.empty() as e:
        print(e)

print("任务完成")

