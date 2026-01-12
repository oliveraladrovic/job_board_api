from pydantic import BaseModel, ConfigDict
from typing import Text

class JobCreate(BaseModel):
    title: str
    description: Text
    company_name: str
    location: str | None = None
    employer_id: int

class JobOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    description: Text
    company_name: str
    location: str | None = None
    employer_id: int