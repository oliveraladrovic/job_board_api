from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from database.base import get_db
from models.jobs import Job
from models.applications import Application
from models.enums import UserRole
from schemas.job import JobCreate, JobOut
from schemas.application import ApplicationOutEmp
from dependencies.roles import require_employer, require_employer_or_admin

router = APIRouter(prefix="/jobs")

@router.post("/", response_model=JobOut, status_code=201)
async def create_job(job_in: JobCreate, db: AsyncSession = Depends(get_db), user = Depends(require_employer_or_admin)):
    new_job = Job(
        title = job_in.title,
        description = job_in.description,
        company_name = job_in.company_name,
        location = job_in.location,
        employer_id = user.id
    )
    db.add(new_job)
    await db.commit()
    await db.refresh(new_job)
    return new_job

@router.get("/my", response_model=list[JobOut])
async def get_my_jobs(db: AsyncSession = Depends(get_db), employer = Depends(require_employer)):
    result = await db.execute(select(Job).where(Job.employer_id == employer.id))
    return result.scalars().all()

@router.get("/{job_id}/applications", response_model=list[ApplicationOutEmp])
async def get_job_applications(job_id: int, db: AsyncSession = Depends(get_db), user = Depends(require_employer_or_admin)):
    # 1) Find Job
    result = await db.execute(select(Job).where(Job.id == job_id))
    job = result.scalar_one_or_none()
    # 2) Must exist
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    # 3) Must be Job "owner" or admin
    if job.employer_id != user.id and user.role != UserRole.admin:
        raise HTTPException(status_code=403, detail="Forbidden")
    # 4) Find all applications
    result = await db.execute(select(Application).options(selectinload(Application.user)).where(Application.job_id == job_id))
    applications = []
    # 5) Structure data for response
    for application in result.scalars().all():
        new_application = {
            "user_id": application.user_id,
            "user_name": application.user.name,
            "status": application.status,
            "applied_at": application.created_at
        }
        applications.append(new_application)
    return applications

@router.get("/{job_id}", response_model=JobOut)
async def get_job_by_id(job_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Job).where(Job.id == job_id))
    job = result.scalar_one_or_none()
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@router.get("/", response_model=list[JobOut])
async def get_jobs(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Job))
    jobs = result.scalars().all()
    return jobs