from contextlib import asynccontextmanager
from fastapi import FastAPI
from database.base import engine
from routers.auth import router as auth_router
from routers.jobs import router as jobs_router
from routers.applications import router as applications_router
from routers.admin import router as admin_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await engine.dispose()

app = FastAPI(lifespan=lifespan)

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(auth_router)
app.include_router(jobs_router)
app.include_router(applications_router)
app.include_router(admin_router)