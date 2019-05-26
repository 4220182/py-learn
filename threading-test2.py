"""
参考：
https://blog.51cto.com/10836356/2176371
https://www.runoob.com/python3/python3-multithreading.html

join()函数的用法:
主线程等待某子线程结束后才能执行,下面的例子就是等m、n线程执行完毕后，最后打印"end";
"""

import threading
import time


class myThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        debug_thread(self.name, self.delay)


def debug_thread(name, delay):
    count = 0
    while count < 2:
        time.sleep(delay)
        count += 1
        print(name, time.ctime(time.time()))


m = myThread('zyh-1', 2)
n = myThread('zyh-2', 4)

m.start()
n.start()
m.join()
n.join()

print("END", time.ctime(time.time()))