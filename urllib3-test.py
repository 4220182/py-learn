"""
利用多线程处理读取的日志：
1. 线程1，把日志读取到队列中
2。 线程2，处理队列中的包含字符"a"的记录，并从队列中删除该记录
3。 线程3，处理队列中的包含字符"b"的记录，并从队列中删除该记录
4。 线程4，处理队列中的包含字符"c"的记录，并从队列中删除该记录

urllib3 参考：https://www.jb51.net/article/143444.htm

"""

import urllib3
import re
import threading

def getContext(url) :
    headers = {
       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }
    http = urllib3.PoolManager();

    r = http.request('get',url,headers = headers)
    return r.data.decode()

def saveContext(url,data) :
    path = "/Users/zyh/tmp/files"
    p = '^http:\\/\\/(.*?)\\/.*?'
    pattern = re.compile(p, re.IGNORECASE)

    m = pattern.match(url)
    if m:
        fname = m.group(1)
    else:
        print("error url !")
        return
    fw = open(path+"/"+fname,"a+")
    try:
        fw.write(data)
    finally:
        fw.close()


urls = ["http://httpbin.org/get"]
for url in urls:
    saveContext(url,getContext(url))


