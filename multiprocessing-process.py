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
当我们在程序中创建进程的时候，子进程复制了父进程及其所有的数据结构，每个子进程有自己独立的内存空间，这也就意味着两个子进程中各有一个counter变量，
所以结果也就可想而知了。要解决这个问题比较简单的办法是使用multiprocessing模块中的Queue类，它是可以被多个进程共享的队列，
底层是通过管道和信号量（semaphore）机制来实现的
multiprocessing.Process 可以直接用multiprocesssing.Queue等进行通信
multiprocessing.Pool不能直接用multiprocessing.Queue进行通信，只能通过共享内存，或者用multiprocessing.Manager()进行进程间通信。

3. 多进程还是多线程:
3.1 计算密集型任务的特点是要进行大量的计算，消耗CPU资源,这类任务用Python这样的脚本语言去执行效率通常很低.
3.2 I/O密集型任务，这类任务的特点是CPU消耗很少，任务的大部分时间都在等待I/O操作完成,时候使用python的多进程和多线程。
"""

import os
import time
from multiprocessing import Process, cpu_count

counter = 0

def run_proc(name):
    global counter
    while counter < 10:
        print(name,counter, end=';', flush=True)
        counter += 1
        time.sleep(0.01)

if __name__ == "__main__":
    ps = []
    #for i in range(cpu_count()):
    for i in range(5):
        p = Process(target=run_proc, args=(i,))
        p.start()
        ps.append(p)
    for i in ps:
        i.join()

    print('All subprocesses done.')