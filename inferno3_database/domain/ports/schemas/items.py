from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from inferno3_database.domain.ports.schemas.objectid import PyObjectId


class Text(BaseModel):
    text: str


class ItemDto(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    type: str
    abilities: Optional[list[str]] = []
    slot: Optional[list[str]] = []
    properties: Optional[list[str]] = []
    level: int
    remort: int
    value: int
    weight: int
    dice: Optional[str] = Field(None)
    damage: Optional[float] = Field(None)
    armor: Optional[int] = Field(None)
    effects: Optional[dict[str, int]] = {}
    prevents: Optional[list[str]] = []
    capacity: Optional[str] = Field(None)
    wand: Optional[str] = Field(None)
    mob: Optional[str] = Field(None)
    room: Optional[str] = Field(None)
    area: Optional[str] = Field(None)
    seller: Optional[str] = Field(None)
    price: Optional[str] = Field(None)

    class Config:
        populate_by_name = True
        from_attributes = True
        json_encoders = {ObjectId: str}
