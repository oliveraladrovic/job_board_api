from contextlib import asynccontextmanager
from fastapi import FastAPI
from database.base import engine
from routers.auth import router as auth_router
from routers.jobs import router as jobs_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await engine.dispose()

app = FastAPI(lifespan=lifespan)

app.include_router(auth_router)
app.include_router(jobs_router)