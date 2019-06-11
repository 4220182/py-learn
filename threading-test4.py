"""
参考：
https://blog.51cto.com/10836356/2176371
https://www.runoob.com/python3/python3-multithreading.html

join()函数的用法:
主线程等待某子线程结束后才能执行,下面的例子就是等m、n线程执行完毕后，最后打印"end";

使用 Thread 对象的 Lock 和 Rlock 可以实现简单的线程同步，这两个对象都有 acquire 方法和 release 方法，
对于那些需要每次只允许一个线程操作的数据，可以将其操作放到 acquire 和 release 方法之间
"""

import threading
import time


class myThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):  # 重写线程run方法
        print("启动线程", self.name)
        threadLock.acquire()
        debug_thread(self.name, self.delay)
        threadLock.release()


def debug_thread(name, delay):
    count = 0
    while count < 10:
        time.sleep(delay)
        count += 1
        print(name, time.ctime(time.time()))

threadLock = threading.Lock()

m = myThread('zyh-1', 1)
n = myThread('zyh-2', 1)

m.start()  # 运行线程
n.start()  # 运行线程

threads = []
threads.append(m)
threads.append(n)

for t in threads :
  t.join()

print("END", time.ctime(time.time()))