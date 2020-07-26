"""
参考：
https://blog.51cto.com/10836356/2176371

"""
import threading
import time
counter = 0
def debug_thread(name,delay) :
    global counter
    while counter < 5 :
        time.sleep(delay)
        counter += 1
        print(name,time.ctime(time.time()))

def debug_thread2(name,delay) :
    global counter
    while True :
        if (counter % 5) == 0 :
            time.sleep(delay)
            print(name,counter,time.ctime(time.time()))

m = threading.Thread(target=debug_thread,args=('zyh-1',2))
n = threading.Thread(target=debug_thread2,args=('zyh-2',4))
m.setName('zyh-1')
n.setName('zyh-2')
m.start()
n.start()

