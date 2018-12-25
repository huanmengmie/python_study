# -*- coding:UTF-8 -*-
from multiprocessing.managers import BaseManager
import queue, random

task_queue = queue.Queue()
result_queue = queue.Queue()


class QueueManager(BaseManager):
    pass


def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


if __name__ == '__main__':

    QueueManager.register("get_task_queue", callable=return_task_queue)
    QueueManager.register("get_result_queue", callable=return_result_queue)

    sever_address = "127.0.0.1"
    manager = QueueManager(address=(sever_address, 5000), authkey=b'123456')
    manager.start()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        num = random.randint(0, 1000)
        print("新建任务，%d的平方是多少？" % num)
        task.put(num)

    print("尝试获取结果：")
    for i in range(10):
        r = result.get(timeout=10)
        print("得到结果：%s" % r)

    # 关闭
    manager.shutdown()
    print("主进程结束")
