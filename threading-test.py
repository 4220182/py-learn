'''
参考：
https://blog.51cto.com/10836356/2176371

'''
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

