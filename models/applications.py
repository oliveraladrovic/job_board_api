from sqlalchemy import UniqueConstraint ,Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy import Enum as SAEnum
from sqlalchemy.orm import relationship
from database.base import Base
from models.enums import ApplicationStatus

class Application(Base):
    __tablename__ = "applications"
    __table_args__ = (
        UniqueConstraint("user_id", "job_id"),
    )
    id = Column(Integer, primary_key=True)
    status = Column(SAEnum(ApplicationStatus, name="application_status"), nullable=False, default=ApplicationStatus.applied)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)
    user = relationship("User", back_populates="applications")
    job = relationship("Job", back_populates="applications")