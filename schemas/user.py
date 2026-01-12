from pydantic import BaseModel, ConfigDict
from models.enums import UserRole

class UserCreate(BaseModel):
    email: str
    hashed_password: str
    role: UserRole
    name: str

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    email: str
    hashed_password: str
    role: UserRole
    name: str