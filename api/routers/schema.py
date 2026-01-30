from pydantic import BaseModel
from typing import List, Optional


class Item(BaseModel): # some request model
    id: int


class ItemCreateRequest(BaseModel):
    new_id: int
    is_admin: Optional[bool] = False

class ItemCreateResponce(BaseModel):
    id: int

    new_id: int
    is_admin: Optional[bool] = False


class ListItems(BaseModel): # some request model
    field: List[Item]
    is_free: bool # Random new field for check
