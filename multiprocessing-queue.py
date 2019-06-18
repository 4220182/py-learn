"""
参考：http://python.jobbole.com/86181/

多进程，共享数据
"""

from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        s = random.random()
        print('Put %s to queue...(%s)' % (value, s))
        q.put(value)
        time.sleep(s)


# 读数据进程执行的代码:
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print('Get %s from queue.' % value)
            time.sleep(2)
        else:
            print('the queue is empty')
            time.sleep(1)


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    pr.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    print('所有数据都写入并且读完')