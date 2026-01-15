from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.base import get_db
from models.applications import Application
from models.jobs import Job
from schemas.application import ApplicationCreate, ApplicationOutCand
from dependencies.roles import require_candidate

router = APIRouter(prefix="/applications")

@router.post("/", response_model=ApplicationOutCand, status_code=201)
async def create_application(application_in: ApplicationCreate, db: AsyncSession = Depends(get_db), candidate = Depends(require_candidate)):
    # 1) Candidate can apply for job only once
    result = await db.execute(select(Application).where(Application.user_id == candidate.id, Application.job_id == application_in.job_id))
    if result.scalar_one_or_none() is not None:
        raise HTTPException(status_code=409, detail="Application already exists")
    # 2) Job must exist
    result = await db.execute(select(Job).where(Job.id == application_in.job_id))
    if result.scalar_one_or_none() is None:
        raise HTTPException(status_code=404, detail="Job not found")
    # 3) Create application
    new_application = Application(
        user_id = candidate.id,
        job_id = application_in.job_id
    )
    db.add(new_application)
    await db.commit()
    await db.refresh(new_application)
    return new_application

@router.get("/my", response_model=list[ApplicationOutCand])
async def get_my_applications(db: AsyncSession = Depends(get_db), candidate = Depends(require_candidate)):
    result = await db.execute(select(Application).where(Application.user_id == candidate.id))
    return result.scalars().all()
