# deploy-service

The service fetches the model artifact from model artifactory service[https://github.com/kumarvikas1/model-artifactory] 

Run Locally

```
minikube start

eval $(minikube docker-env)

docker build -t deploy-service:1 .

cd kubernetes

kubectl apply -f rbac.yaml

kubectl apply -f deployment.yaml
```

Test-
You will need to update your hosts file for below host name

```
http://dev.xgboostdemo.com/deploy-service/xgboost-demo
```
