from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    print("Got a root request!")
    return {"message": "Hello World"}


@app.post("/")
async def root(data: str):
    print(f"Got POST on root!\nData sent: {data}")
    return {"responce": "Ok!", "data_responce": data}


if __name__ == "__main__":
    uvicorn.run("s1:app", host="0.0.0.0", port=8000, reload=True)
