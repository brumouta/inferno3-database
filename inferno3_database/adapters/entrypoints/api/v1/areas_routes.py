import json

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette.requests import Request
from starlette.responses import Response


router = APIRouter()


@router.get("/", response_model=list[str])
async def list_areas(request: Request):
    return Response(
        content=json.dumps(
            jsonable_encoder(
                list(filter(None, await request.app.db.items.distinct("area")))
            )
        ),
        status_code=200,
    )
