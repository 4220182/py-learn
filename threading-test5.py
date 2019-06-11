"""
利用多线程处理读取网站的内容，并写入文件中：

urllib3 参考：https://www.jb51.net/article/143444.htm

get测试站点：
http://httpbin.org/get

我们在函数中使用：time.sleep(30)，让程序等待30秒。
测试结果，可以看出，如果函数处理的时间比较长的话，多线程速度更加快：
单线程：
real	2m44.751s
user	0m0.172s
sys	0m0.030s

多线程：
real	0m35.373s
user	0m0.198s
sys	0m0.050s


"""

import urllib3
import re
import threading
import random
import string
import certifi
import time
def getContext(url,data) :
    print("http starging "+ url)
    headers = {
       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where());

    r = http.request('get',url,headers = headers)
    print("http end " + url)
    saveContext(url,r.data.decode())

def saveContext(url,data) :
    print("write file staring: "+url)
    path = "/Users/zyh/tmp/files"
    p = '^http(|s):\\/\\/(.*?)\\/.*?'
    pattern = re.compile(p, re.IGNORECASE)

    m = pattern.match(url)
    if m:
        fname = m.group(2)
    else:
        print("error url !")
        return
    fw = open(path+"/"+fname,"a+")
    try:
        fw.write(url+"\n")
    finally:
        fw.close()
    time.sleep(30)
    print("write file end: "+url)

urls = []

# 随机生成1000个网址，并放进数组中
i = 0
while i < 5 :
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    urls.append("https://amazonaws-china.com/cn/" + ran_str)
    i += 1

# 单线程处理：
# for url in urls:
#     getContext(url,"data")

# 多线程处理：
threadList = []
for url in urls:
    print("new Tread staring: " + url)
    m = threading.Thread(target=getContext, args=(url,"data"))  # 为啥不能使用一个参数？
    m.setName(url)
    threadList.append(m)
    print("new Thread end: "+url)

for t in threadList:
    t.start()  # 运行线程
    print("thread start: "+ t.getName())

for t in threadList:
    t.join()

print("finished")


