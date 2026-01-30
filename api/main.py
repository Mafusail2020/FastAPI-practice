from fastapi import FastAPI
import uvicorn

from routers.router import router

app = FastAPI() # or just pass at the start
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
