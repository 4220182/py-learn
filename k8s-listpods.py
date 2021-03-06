'''
安装：
$ sudo pip3.6 install kubernetes

api 文档：
https://github.com/kubernetes-client/python/blob/master/kubernetes/README.md

list pods :
https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/CoreV1Api.md#list_pod_for_all_namespaces
'''
from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name,i.status.phase))
