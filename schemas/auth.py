from pydantic import BaseModel
from models.enums import UserRole

class LoginIn(BaseModel):
    email: str
    password: str

class LoginOut(BaseModel):
    access_token: str
    token_type: str

class NewRole(BaseModel):
    role: UserRole