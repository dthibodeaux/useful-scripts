# Here we deploy argoCD in a K8s cluster:
--

- Create namespace:
    
    `kubectl create namespace argocd`

- Download and Review Manifest:

    `curl -O https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml`

- Deploy Manfest Yaml (https://argo-cd.readthedocs.io/en/stable/getting_started/):

    `kubectl apply -n argocd -f install.yaml`

- [Optional] Review Deployments Created By `install.yaml`:

    `kubectl get deployment -n argocd`

```
NAME                               READY   UP-TO-DATE   AVAILABLE   AGE
argocd-applicationset-controller   1/1     1            1           108s
argocd-dex-server                  1/1     1            1           108s
argocd-notifications-controller    1/1     1            1           108s
argocd-redis                       1/1     1            1           108s
argocd-repo-server                 1/1     1            1           108s
argocd-server                      1/1     1            1           108s
```

- [Optional] Review Services Created By `install.yaml`:

    `kubectl get service -n argocd`

```
NAME                                      TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                      AGE
argocd-applicationset-controller          ClusterIP   10.99.1.75       <none>        7000/TCP,8080/TCP            4m31s
argocd-dex-server                         ClusterIP   10.110.104.43    <none>        5556/TCP,5557/TCP,5558/TCP   4m30s
argocd-metrics                            ClusterIP   10.106.97.68     <none>        8082/TCP                     4m30s
argocd-notifications-controller-metrics   ClusterIP   10.111.22.130    <none>        9001/TCP                     4m30s
argocd-redis                              ClusterIP   10.105.138.198   <none>        6379/TCP                     4m30s
argocd-repo-server                        ClusterIP   10.97.9.141      <none>        8081/TCP,8084/TCP            4m30s
argocd-server                             ClusterIP   10.98.228.130    <none>        80/TCP,443/TCP               4m30s
argocd-server-metrics                     ClusterIP   10.105.92.56     <none>        8083/TCP                     4m30s
```

- [Optional] Review StatefulSet Created By `install.yaml`:

    `kubectl get statefulset -n argocd`

## Install ArgoCD CMDline:
- MAC OS:
    `brew install argocd`
- Others: https://argo-cd.readthedocs.io/en/stable/cli_installation/

```
#CMD$$> argocd version
argocd: v2.12.3+6b9cd82
  BuildDate: 2024-08-27T15:58:49Z
  GitCommit: 6b9cd828c6e9807398869ad5ac44efd2c28422d6
  GitTreeState: clean
  GoVersion: go1.23.0
  Compiler: gc
  Platform: darwin/amd64
FATA[0000] Argo CD server address unspecified 

##argocd version --client
argocd: v2.12.3+6b9cd82
  BuildDate: 2024-08-27T15:58:49Z
  GitCommit: 6b9cd828c6e9807398869ad5ac44efd2c28422d6
  GitTreeState: clean
  GoVersion: go1.23.0
  Compiler: gc
  Platform: darwin/amd64
```
## To use outside of cluster = Expose the API services with a Patch:
- `kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "NodePort"}}'` -- Expose to external connections: 

```
##> kubectl get service -n argocd
argocd-server                             NodePort    10.98.228.130    <none>        80:30231/TCP,443:30898/TCP   29m
```

- `kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'` -- CloudServices

- Expose/Forward port from control node with NodePort and by-pass tls.
`kubectl port-forward svc/argocd-server -n argocd 8080:443 --address 192.168.1.91 --insecure-skip-tls-verify`

```
# Useful Doc an login URLS:

 https://192.168.1.91:8080/login?return_url=https%3A%2F%2F192.168.1.91%3A8080%2Fapplications

https://kubernetes.io/docs/reference/kubectl/generated/kubectl_port-forward/

```
## Decode password for UI login:

- `kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d && echo`
