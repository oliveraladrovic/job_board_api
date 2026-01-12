from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    name = Column(String, nullable=False)
    jobs = relationship("Job", back_populates="employer")
    applications = relationship("Application", back_populates="user")