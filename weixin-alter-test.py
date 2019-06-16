"""
发送信息到企业微信

企业微信管理网址：
https://work.weixin.qq.com


参考：
https://work.weixin.qq.com/api/doc#90000/90003/90487
https://work.weixin.qq.com/api/doc#90000/90135/90236
http://www.ttlsa.com/zabbix/use-wechat-send-zabbix-msg/

json 参考：
https://www.cnblogs.com/OnlyDreams/p/7850920.html
"""

import urllib3
import json

urllib3.disable_warnings()
def getContext(url) :
    headers = {
       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }
    http = urllib3.PoolManager();

    r = http.request('get',url,headers = headers)
    return r.data.decode()

def postContext(url,agentid)  :
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Content-type': 'application/json'
    }
    http = urllib3.PoolManager();
    body = {
        'touser': '@all',
        'msgtype': 'text',
        'agentid': agentid,
        'text': {"content": '这是一个测试2'},
        'safe': 0
        }
    print(body)
    r = http.request('post', url, headers=headers, body=json.dumps(body).encode('utf-8'))
    return r.data.decode()

AgentId = 1000002
Secret = "bMTmFmjChbAxxxxxxxxxxxxxVeSR2k8QT8"
corpId = "xxxxxxxxxxxxxxxx"

getTokenUrl = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid="+corpId+"&corpsecret="+Secret
tokenMessage = json.loads(getContext(getTokenUrl))
access_token = tokenMessage['access_token']
print(access_token)

posturl = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+access_token
result = postContext(posturl, AgentId)
print(result)


