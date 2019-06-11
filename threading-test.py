"""
参考：
https://blog.51cto.com/10836356/2176371

Python的多线程不是类似java的多线程，Python有一个全局锁机制，多个线程其实并不是并行执行（是不是并发更准确？），而是轮换执行，况且不能有效利用多核.

"""
import threading
import time

def debug_thread(name,delay) :
    count = 0
    while count < 5 :
        time.sleep(delay)
        count += 1
        print(name,time.ctime(time.time()))

m = threading.Thread(target=debug_thread,args=('zyh-1',2))
n = threading.Thread(target=debug_thread,args=('zyh-2',4))
m.setName('zyh-1')
n.setName('zyh-2')
m.start()
n.start()

