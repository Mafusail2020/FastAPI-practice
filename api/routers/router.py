from fastapi import APIRouter
from routers.schema import (
    Item, 
    ListItems,
    ItemCreateRequest,
    ItemCreateResponce
)


router = APIRouter()

@router.get("/")
async def root():
    print("Got a root router request!")
    return {"message": "Hello World"}

# GET ITEMS
@router.get("/list", response_model=ListItems)
async def get_items_list():
    or_like_this = Item(id=2)

    return {
        "field": [
        {"id": 1}, 
        or_like_this
        ], # both are passing, because both meet Item schema List[Item]
        "is_free": True
    } 


@router.get("/{some_id}")
async def get_some_id(some_id: int)->Item:
    print("Get_id")
    return {"id": some_id}


# SET ITEMS
@router.post("/create_id", response_model=ItemCreateResponce)
async def set_some_id(payload: ItemCreateRequest):
    print(payload)

    data = payload.model_dump() # payload -> dict
    print(data)
    return {"id": 123, **data}


# PUT ITEMS
@router.put("/{some_id}", response_model=Item)
async def update_id(some_id: int, data: dict):
    print(data)
    return {"id": some_id}
