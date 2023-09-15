import json
from enum import Enum

from fastapi import APIRouter, Response

router = APIRouter()


class StatusEnum(str, Enum):
    OK = "OK"
    FAILURE = "FAILURE"
    CRITICAL = "CRITICAL"
    UNKNOWN = "UNKNOWN"


@router.get("/")
def health() -> Response:
    return Response(
        content=json.dumps(StatusEnum.OK),
        media_type="application/json",
        status_code=200,
    )
