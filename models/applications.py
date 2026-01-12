from sqlalchemy import UniqueConstraint ,Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base

class Application(Base):
    __tablename__ = "applications"
    __table_args__ = (
        UniqueConstraint("user_id", "job_id"),
    )
    id = Column(Integer, primary_key=True)
    status = Column(String, nullable=False, default="applied")
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)
    user = relationship("User", back_populates="applications")
    job = relationship("Job", back_populates="applications")