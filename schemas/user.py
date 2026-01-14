from pydantic import BaseModel, ConfigDict
from typing import Literal
from models.enums import UserRole

class UserCreate(BaseModel):
    email: str
    password: str
    role: Literal["candidate", "employer"]
    name: str

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    email: str
    role: UserRole
    name: str