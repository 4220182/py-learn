'''
https://stackoverflow.com/questions/48687153/where-can-i-get-the-api-key-in-kubernetes-installation

get token:
$ kubectl get secrets -n kube-system
$ kubectl describe secret/{secret_name} -n kube-system
'''

from kubernetes import client, config
from kubernetes.client.rest import ApiException
ApiToken = 'xxx'
configuration = client.Configuration()
configuration.host = 'https://192.168.0.110:6443'
configuration.verify_ssl=False
configuration.debug = True
configuration.api_key={"authorization":"Bearer "+ ApiToken}
client.Configuration.set_default(configuration)
kubeApi = client.CoreV1Api()
try:
    allPods = kubeApi.list_pod_for_all_namespaces(watch=False)
except ApiException as e:
    print("Exception when calling CoreV1Api->list_pod_for_all_namespaces: %s\n" % e)
