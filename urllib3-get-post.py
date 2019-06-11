"""
urllib3 参考：https://www.jb51.net/article/143444.htm

Beautiful Soup ：
参考：https://www.jb51.net/article/143229.htm
是一个可以从 HTML 或 XML 文件中提取数据的 Python 库，它能够通过你喜欢的转换器实现惯用的文档导航、查找、修改文档的方式，能够帮你节省数小时甚至数天的工作时间。

测试网址：http://httpbin.org
get ： http://httpbin.org/get
post form ：http://httpbin.org/forms/post
post action : http://httpbin.org/post
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

def postContext(url)  :
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }
    http = urllib3.PoolManager();
    fields = {
        'custname': 'test-name',
        'test-name': 'hello',
        'custtel': '13888888888',
        'custemail': '13888888888@gmail.com'
    }
    r = http.request('post', url, headers=headers, fields=fields)
    return r.data.decode()


geturl = "http://httpbin.org/get"
posturl = "http://httpbin.org/post"

print(postContext(posturl))

