"""
pool创建子进程的方法与Process不同，是通过p.apply_async(func,args=(args))实现，
一个池子里能同时运行的任务是取决你电脑的cpu数量，如我的电脑现在是有4个cpu，
那会子进程task0,task1,task2,task3可以同时启动，task4则在之前的一个某个进程结束后才开始

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

3. 分布式进程
如果愿意还可以将多个进程部署在不同的计算机上，做成分布式进程，
具体的做法就是通过multiprocessing.managers模块中提供的管理器将Queue对象通过网络共享出来（注册到网络上让其他计算机可以访问），
这部分内容也留到爬虫的专题再进行讲解。
参考：https://github.com/jackfrued/Python-100-Days/blob/master/Day66-75/69.%E5%B9%B6%E5%8F%91%E4%B8%8B%E8%BD%BD.md
"""

import os
import time
from multiprocessing import Pool, cpu_count


def run_proc(name):
    print("run child process: %s, %d" % (name, os.getpid()))
    time.sleep(10)
    print("finish child process: %s, %d" % (name, os.getpid()))


if __name__ == "__main__":
    q = Pool()
    #for i in range(cpu_count()):
    for i in range(20):
        q.apply_async(run_proc, args=(i,))

    print('Waiting for all subprocesses done...')
    q.close()
    q.join()
    print('All subprocesses done.')