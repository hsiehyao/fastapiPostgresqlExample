import uvicorn
from fastapi import FastAPI

from db import database
from resource.routes import api_router

app = FastAPI()
app.include_router(api_router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def startup():
    await database.disconnect()


if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0", port=8000, reload=True)
