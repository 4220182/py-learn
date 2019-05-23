'''
安装：
$ sudo pip3.6 install kubernetes

api 文档：
https://github.com/kubernetes-client/python/blob/master/kubernetes/README.md

get pod status :
https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/CoreV1Api.md#read_namespaced_pod_status
'''
from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")

pod_name='curl-7cb5f8c5fc-nwgxx'
resp = v1.read_namespaced_pod_status(pod_name, 'default')
print(pod_name,resp.status.host_ip,resp.status.pod_ip,resp.status.phase)
