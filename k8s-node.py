'''
文档：
https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/CoreV1Api.md#list_node
'''
from __future__ import print_function
from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()

for node in v1.list_node().items:
    print(node.metadata.name,node.status.phase,node.status.addresses,node.status.capacity,node.status.allocatable)