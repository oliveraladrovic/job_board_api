from sqlalchemy import Column, Integer, String, Text, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    company_name = Column(String, nullable=False)
    location = Column(String)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    employer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    employer = relationship("User", back_populates="jobs")
    applications = relationship("Application", back_populates="job")