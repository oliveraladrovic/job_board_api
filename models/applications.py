from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.base import Base

class Application(Base):
    __tablename__ = "applications"
    id = Column(Integer, primary_key=True)
    status = Column(String, nullable=False, default="applied")
    created_at = Column(datetime, nullable=False)
    user_id = Column(Integer, ForeignKey="users.id", nullable=False)
    job_id = Column(Integer, ForeignKey="jobs.id", nullable=False)
    user = relationship("User", back_populates="applications")
    job = relationship("Job", back_populates="applications")