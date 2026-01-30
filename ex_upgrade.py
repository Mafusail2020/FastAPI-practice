from typing import Union, Any

from fastapi import FastAPI
import uvicorn

from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: Any, q: Union[str, None] = None, k: Union[str, None] = None):
    return {"item_id": item_id, "q": q, "k": k}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


if __name__ == "__main__":
    uvicorn.run("ex_upgrade:app", host="0.0.0.0", port=8000, reload=True)
