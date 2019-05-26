import _thread
import time

def debug_thread(name,delay) :
    count = 0
    while count < 1000 :
        time.sleep(delay)
        count += 1
        print(name,time.ctime(time.time()))

try :
    _thread.start_new_thread(debug_thread,("name-1",2))
    _thread.start_new_thread(debug_thread, ("name-2",4))
    _thread.start_new_thread(debug_thread, ("name-3", 5))

except :
    print("error")

while 1:
    pass
