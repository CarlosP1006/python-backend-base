from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src.infra.containers.app_container import container

router = APIRouter()


@router.get("/random")
def get_random():
  body = container.get_random_service().execute()
  return JSONResponse(status_code=status.HTTP_200_OK, content=body)