from fastapi import APIRouter


router = APIRouter()

@router.get("/")
async def root():
    print("Got a root router request!")
    return {"message": "Hello World"}


@router.post("/")
async def root(data: str):
    print(f"Got POST on router root!\nData sent: {data}")
    return {"responce": "Ok!", "data_responce": data}


@router.get("/{some_id}")
async def get_some_id(some_id: int):
    print("Get_id")
    return {"id": some_id}
