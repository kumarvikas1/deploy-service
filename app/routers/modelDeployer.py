from fastapi import APIRouter
from .service.deploymentService import DeploymentService
from .service.serviceDeployer import ServiceDeployer
from .service.ingressDeployer import IngressDeployer
router = APIRouter()

@router.get(path='/deploy-service/{model_name}')
def create_model(model_name):
    try:
        DeploymentService.deploy_service(model_name)
        ServiceDeployer.service_deploy(model_name)
        IngressDeployer.ingress_deploy(model_name)
    except Exception as err:
        raise err
