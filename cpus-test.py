"""
测试利用多核cpu ：
参考： https://blog.csdn.net/weixin_43258754/article/details/83552484

在Python里推荐使用多进程而不是多线程:
https://blog.csdn.net/longdreams/article/details/78195403
"""

import time
from multiprocessing import Process

# 定义CPU密集型函数
def count(x, y):
    c = 0
    while c < 500000:
        c += 1
        x += x
        y += y

#定义IO密集型函数
def write():
    f = open("/tmp/test.txt", "w")
    for x in range(500000):
        f.write("testwrite\n")
    f.close()
def read():
    f = open("/tmp/test.txt", "r")
    lines = f.readlines()
    f.close()

# CPU密集操作
t = time.time()
for x in range(10):
    count(1, 1)
print("cpu函数运行时间：", time.time() - t)

# # IO密集操作
# t = time.time()
# for x in range(10):
#     write()
#     read()
# print("IO函数运行时间：", time.time() - t)

# counts = []
# t = time.time()
# for x in range(10):
#     process = Process(target=count, args=(1,1))
#     counts.append(process)
#     process.start()
# e = counts.__len__()
# while True:
#     for i in counts:
#         if not i.is_alive():
#             e -= 1
#     if e <= 0:
#         break
# print(time.time() - t)