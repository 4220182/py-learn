"""
cpu_count: 计算机的cpu核心数

参考：
http://python.jobbole.com/86181/

multiprocessing.Process，multiprocessing.Pool区别 ：
参考：https://blog.csdn.net/eldencheng/article/details/80896128

1. 是否可以批量开启子进程
multiprocessing.Process 可以批量开启子进程
multiprocessing.Pool可以批量开启子进程（cpu有多少个核,就批量启动多少个子进程，如果启动的数量超过cpu核心数，就需要等待。）

2. 进程间通信
multiprocessing.Process 可以直接用multiprocesssing.Queue等进行通信
multiprocessing.Pool不能直接用multiprocessing.Queue进行通信，只能通过共享内存，或者用multiprocessing.Manager()进行进程间通信。
"""

import os
import time
from multiprocessing import Process, cpu_count


def run_proc(name):
    print("run child process: %s, %d" % (name, os.getpid()))
    time.sleep(10)
    print("finish child process: %s, %d" % (name, os.getpid()))


if __name__ == "__main__":
    ps = []
    #for i in range(cpu_count()):
    for i in range(20):
        p = Process(target=run_proc, args=(i,))
        p.start()
        ps.append(p)
    for i in ps:
        i.join()

    print('All subprocesses done.')