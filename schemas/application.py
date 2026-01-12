from pydantic import BaseModel, ConfigDict
from models.enums import ApplicationStatus

class ApplicationCreate(BaseModel):
    status: ApplicationStatus
    user_id: int
    job_id: int

class ApplicationOut(BaseModel):
    id: int
    status: ApplicationStatus
    user_id: int
    job_id: int