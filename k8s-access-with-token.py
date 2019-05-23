'''
https://stackoverflow.com/questions/48687153/where-can-i-get-the-api-key-in-kubernetes-installation

get token:
$ kubectl get secrets -n kube-system
$ kubectl describe secret/{secret_name} -n kube-system

api 参考：
https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/CoreV1Api.md#list_pod_for_all_namespaces
'''

from kubernetes import client, config
from kubernetes.client.rest import ApiException
import urllib3

urllib3.disable_warnings()

ApiToken = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJ0aWxsZXItdG9rZW4tZ2o4ajciLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoidGlsbGVyIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQudWlkIjoiNzY2YWRmODktNDhhMS0xMWU5LWFkMjgtMDgwMDI3YmZiNTUwIiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50Omt1YmUtc3lzdGVtOnRpbGxlciJ9.CXzwZNxU8ALw7wkMlvPgrT2c0h7MZZwuUUEFddiGsga0EgS3ZOV8oGC-ES2bxs8o_6RlbCKvv8D_2Ol3ApfNN_ZfgFVYtXmeHJlblbeEMvMbOTtjO6h4PrsKbW7VMT6RNDuT3UOqrZ0hquPKIowMo3GnN-iK3ZT8SN4w185ebHLoU-m2KIm5ljansuphCnCZyak9C7JpEZHXjYx8KJ_bNbrty3c1w7h5sd98frll3-_IwZRYzDibIv5rmDf7fZ_hRPo8Iyj69vixyVpaGR4lP63ypa_0pgSY607-JP3NvMJGQ9bCIAQHCyQuJa6F4fkD0NlBLPiMUwrsoe6ZTUPhig'
configuration = client.Configuration()
configuration.host = 'https://10.2.2.120:6443'
configuration.verify_ssl=False
configuration.debug = True
configuration.api_key={"authorization":"Bearer "+ ApiToken}
client.Configuration.set_default(configuration)
kubeApi = client.CoreV1Api()
try:
    allPods = kubeApi.list_pod_for_all_namespaces(watch=False)
    for item in allPods.items :
        print(item.metadata.name, item.status.pod_ip,item.status.container_statuses[0])

except ApiException as e:
    print("Exception when calling CoreV1Api->list_pod_for_all_namespaces: %s\n" % e)

