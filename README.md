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

You should have your model ready to be served using a random feature values

```
curl http://dev.xgboostdemo.com/sampling-service/xgboost-demo/predict
```

You can also send model input feature values

```
curl --location --request POST 'http://dev.xgboostdemo.com/sampling-service/xgboost-demo/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
    "features": [[0.4886530794542341, 0.9931183497579041, 0.5521141503801427]]
}'
```
