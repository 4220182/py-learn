"""
一个几十G的文件想用Python解决方案，

方法一：利用awk对文件进行“模数切割”，Mod的不同余数分别对应一个处理线程。

targetFile=xxx
threadNum=5    # 设定五个线程
for((i=0; i<threadNum; i++))
do
    awk 'NR%n==t {print $0}' n=$threadNum t=$i $targetFile | python doTask.py &
done

方法二：多线程处理
https://www.jb51.net/article/156084.htm

下面利用方法二，处理大文件的读写

https://www.runoob.com/python3/python3-multithreading.html
"""

from threading import Thread
import threading
import os

logfile = "logs/users.log"

def ReadTimes():
    res = []
    if os.path.exists(logfile):
        fp = open(logfile, 'r')
    else:
        os.system(logfile)
        fp = open(logfile, 'r')
    try:
        line = fp.read()
        if line == None or len(line) == 0:
            fp.close()
            return 0
        tmp = line.split()
        print
        'tmp: ', tmp
        schedule_times = int(tmp[-1])
    finally:
        fp.close()
    # print schedule_times
    return schedule_times


def WriteTimes(schedule_times):
    if schedule_times <= 10:
        fp = open(logfile, 'a+')  # 10以内追加进去
    else:
        fp = open(logfile, 'w')  # 10以外重新写入
        schedule_times = 1
    print('write schedule_times start!')
    try:

        fp.write(str(schedule_times) + '\n')
    finally:
        fp.close()
        print('write schedule_times finish!')


# 2、加锁
mu = threading.Lock()  # 1、创建一个锁


def lock_test():
    # time.sleep(0.1)
    if mu.acquire(True):  # 2、获取锁状态，一个线程有锁时，别的线程只能在外面等着
        schedule_times = ReadTimes()
        print
        schedule_times
        schedule_times = schedule_times + 1
        WriteTimes(schedule_times)
        mu.release()  # 3、释放锁


if __name__ == '__main__':

    for i in range(500000000):
        Thread(target=lock_test, args=()).start()