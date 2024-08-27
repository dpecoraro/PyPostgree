from contextlib import asynccontextmanager

from fastapi import FastAPI
from uvicorn import lifespan

from Infra.startup_handle import recreate_tables
from Infra.database_conn import engine
from routes import staff_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    await recreate_tables(engine)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(staff_routes.router)
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
