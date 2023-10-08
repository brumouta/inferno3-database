import json

from fastapi import APIRouter, Response
from fastapi.encoders import jsonable_encoder
from starlette.requests import Request

from inferno3_database import text_parser, item_parser
from inferno3_database.domain.ports.schemas.items import ItemDto, Text


router = APIRouter()


@router.get("/", response_model=list[ItemDto])
async def list_items(request: Request):
    return Response(
        content=json.dumps(
            jsonable_encoder(await request.app.db.items.find().to_list(length=100))
        ),
        # content=json.dumps(jsonable_encoder(await request.app.db.items.count_documents({}))),
        status_code=200,
    )


@router.post("/", response_model=list[ItemDto])
async def insert_item(request: Request, text: Text):
    unparsed_items = text_parser.parse_items(text.text)
    items: list[ItemDto] = []
    for unparsed in unparsed_items:
        parsed_item = item_parser.parse_item(unparsed)
        items.append(jsonable_encoder(parsed_item))
    await request.app.db.items.insert_many(items)

    return Response(
        content=json.dumps(jsonable_encoder({"items": items})),
        status_code=201,
    )


@router.options("/", status_code=204)
async def options() -> Response:
    return Response(
        headers={
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
            "Access-Control-Allow-Origin": "*",
        },
        status_code=204,
    )
