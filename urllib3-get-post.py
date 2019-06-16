"""
urllib3 参考：
https://www.jianshu.com/p/df9b883fecae
https://www.jb51.net/article/143444.htm

测试网址：http://httpbin.org
get ： http://httpbin.org/get
post form ：http://httpbin.org/forms/post
post action : http://httpbin.org/post
"""

import urllib3
import re
import threading
import json
def getContext(url) :
    headers = {
       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }
    http = urllib3.PoolManager();

    r = http.request('get',url,headers = headers)
    return r.data.decode()

def postContext(url)  :
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Content-type': 'application/json'
    }
    http = urllib3.PoolManager();
    fields = {
        'custname': 'test-name',
        'test-name': 'hello',
        'custtel': '13888888888',
        'data': {'context': 'just a test'},
        'custemail': '13888888888@gmail.com'
    }
    #r = http.request('post', url, headers=headers, fileds=fields) #fields里面嵌套了字典，会报错，改为下面就好了
    r = http.request('post', url, headers=headers, body=json.dumps(fields).encode('utf-8'))
    return r.data.decode()


geturl = "http://httpbin.org/get"
posturl = "http://httpbin.org/post"

print(postContext(posturl))

