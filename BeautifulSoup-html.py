"""

Beautiful Soup ：
参考：
https://www.jb51.net/article/143229.htm
https://blog.csdn.net/love666666shen/article/details/77512353

是一个可以从 HTML 或 XML 文件中提取数据的 Python 库，它能够通过你喜欢的转换器实现惯用的文档导航、查找、修改文档的方式，能够帮你节省数小时甚至数天的工作时间。

Beautiful Soup是python的一个库，最主要的功能是从网页抓取数据.
Beautiful Soup提供一些简单的、python式的函数用来处理导航、搜索、修改分析树等功能。它是一个工具箱，
   通过解析文档为用户提供需要抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序。
Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。你不需要考虑编码方式，
   除非文档没有指定一个编码方式，这时，Beautiful Soup就不能自动识别编码方式了。然后，你仅仅需要说明一下原始编码方式就可以了。
Beautiful Soup已成为和lxml、html6lib一样出色的python解释器，为用户灵活地提供不同的解析策略或强劲的速度。

BeautifulSoup 不仅支持 HTML 解析器，还支持一些第三方的解析器，如 lxml，XML，html5lib 但是需要安装相应的库。如果我们不安装，
   则 Python 会使用 Python 默认的解析器，其中 lxml 解析器更加强大，速度更快，推荐安装。

$ pip install beautifulsoup4
$ pip install html5lib
$ pip install lxml

"""

import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings() #禁用各种警告
def getContext(url) :
    headers = {
       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }
    http = urllib3.PoolManager();
    r = http.request('get',url,headers = headers)
    return r.data.decode()


geturl = "https://www.baidu.com/"
html_doc = getContext(geturl)
soup = BeautifulSoup(html_doc, "lxml")

print(soup.title)
print(soup.title.string)
print(soup.find_all(id='result_logo'))
print("---a---")
for a in soup.find_all('a'):
    print(a, a['href'], a.get_text())
    print(a.attrs)
