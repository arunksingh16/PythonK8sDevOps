# Code for Iterating namespaces
from kubernetes import client, config, watch
from kubernetes.client import configuration
from prettytable import PrettyTable
from kubernetes.client.rest import ApiException


def main():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    #print(dir(v1))

    ns = ['namespace-x','namespace-y']
    for ns_v in ns:
        print('Namespace: ' + ns_v)
        ret = v1.list_namespaced_pod(ns_v)
        #dir(ret) see methods/vars
        t = PrettyTable(['POD Name','POD status','POD IP','Status Reason','Namespace','Node'])
        for pod in ret.items:
            t.add_row([pod.metadata.name, pod.status.phase, pod.status.pod_ip, pod.status.reason, pod.metadata.namespace, pod.spec.node_name])

        print(t)
        print()


if __name__ == '__main__':
    main()
