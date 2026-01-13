from pydantic import BaseModel, ConfigDict
from datetime import datetime
from models.enums import ApplicationStatus

class ApplicationCreate(BaseModel):
    job_id: int

class ApplicationOutCand(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    status: ApplicationStatus
    user_id: int
    job_id: int

class ApplicationOutEmp(BaseModel):
    user_id: int
    user_name: str
    status: ApplicationStatus
    applied_at: datetime