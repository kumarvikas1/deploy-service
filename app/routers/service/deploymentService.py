from jinja2 import Environment, FileSystemLoader
import requests as req
import json
from fastapi import HTTPException
from .token.tokenProvider import get_token
env = Environment(loader=FileSystemLoader('./templates'), trim_blocks=True, lstrip_blocks=True)


class DeploymentService:

    def deploy_service(modelname):
        try:
            template = env.get_template('deployment.j2')
            dep = template.render(model_name=modelname, image_name='xgboost-base-image',
                              image_version='1')
            res = req.post("https://kubernetes.default.svc/apis/apps/v1/namespaces/ml-demo/deployments", json=json.loads(dep),
                          headers={"Authorization": get_token()}, verify=False)
            status = res.status_code
            if status != 201:
                print(f"error {res.content}")
                raise NameError(f"kubernetes status was {status}")
            return f"Deployment successfully created with status {status}"
        except Exception as err:
            print(err)
            raise HTTPException(status_code=500, detail=f"Error occured {err}")
