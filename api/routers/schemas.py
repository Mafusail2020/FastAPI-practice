from pydantic import BaseModel


class Item(BaseModel): # some request model
    id: int
