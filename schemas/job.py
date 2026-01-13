from pydantic import BaseModel, ConfigDict

class JobCreate(BaseModel):
    title: str
    description: str
    company_name: str
    location: str | None = None

class JobOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    description: str
    company_name: str
    location: str | None = None
    employer_id: int