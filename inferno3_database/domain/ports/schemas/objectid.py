from typing import Any, Dict

from bson import ObjectId
from pydantic import GetJsonSchemaHandler
from pydantic_core import CoreSchema


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(
        cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler
    ) -> Dict[str, Any]:
        json_schema = super().__get_pydantic_json_schema__(core_schema, handler)
        json_schema = handler.resolve_ref_schema(json_schema)
        json_schema.update(type="string")
        return json_schema
