'''
文档： https://github.com/kubernetes-client/python/blob/master/kubernetes/README.md

https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/ApisApi.md#get_api_versions
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
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApisApi->get_api_versions: %s\n" % e)