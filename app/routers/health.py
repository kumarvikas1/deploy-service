from fastapi import APIRouter

router = APIRouter()


@router.get(path='/deploy-service/isActive')
async def is_active():
    return True


@router.get(path='/deploy-service/ping')
async def ping():
    return 'pong'