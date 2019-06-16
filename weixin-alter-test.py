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

问题：
1. 目前发送到部门，如果内容是中文，就会显示乱码；发送到@all，就不会是乱码
   百度搜：urllib3 企业微信发消息乱码
   解决此问题，改用 requests 库（还没测试）
参考：
https://www.jianshu.com/p/084d6bf2bdea
https://cloud.tencent.com/developer/news/272595
"""

import urllib3
import json

urllib3.disable_warnings()
def getContext(url) :
    headers = {
       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }
    http = urllib3.PoolManager();

    r = http.request('get', url, headers=headers)
    return r.data.decode()


def postContext(url, agentid):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Content-type': 'application/json; charset=utf-8'
    }
    http = urllib3.PoolManager()
    message = "我爱祖国"
    body = {
        'touser': '@all', #向用户发送信息
        #'toparty': 2, #向部门发送信息，填写部门ID
        'msgtype': 'text',
        'agentid': agentid,
        'text': {"content": message},
        'safe': 0
        }
    message_body = bytes(json.dumps(body), 'utf-8')
    r = http.request('post', url, headers=headers, body=message_body)
    return r.data.decode()

AgentId = 1000002
Secret = "xxxxxxxxx"
corpId = "xxxxxxxxx"

getTokenUrl = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid="+corpId+"&corpsecret="+Secret
tokenMessage = json.loads(getContext(getTokenUrl))
access_token = tokenMessage['access_token']
print("access_tokey:", access_token)

posturl = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+access_token
result = postContext(posturl, AgentId)
print("result: %s" % (result))


