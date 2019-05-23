'''
文档： https://github.com/kubernetes-client/python/blob/master/kubernetes/README.md

参考：
https://stackoverflow.com/questions/48687153/where-can-i-get-the-api-key-in-kubernetes-installation

参考：https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/ApisApi.md#get_api_versions
改动可以运行的例子
'''
from __future__ import print_function

from kubernetes import client, config

import kubernetes.client

from kubernetes.client.rest import ApiException
from pprint import pprint

config.load_kube_config()

api_instance = kubernetes.client.ApisApi(kubernetes.client.ApiClient())

try:
    api_response = api_instance.get_api_versions()
except ApiException as e:
    print("Exception when calling ApisApi->get_api_versions: %s\n" % e)

print("ok")