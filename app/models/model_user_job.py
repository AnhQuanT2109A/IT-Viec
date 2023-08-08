from app.models.model_base import BareBaseModel
from sqlalchemy import Column, String, Date, Integer, ForeignKey
from sqlalchemy.orm import relationship
class User_Job(BareBaseModel):
    full_name = Column(String(255), index=True)
    phone = Column(String, index=True)
    date_of_birth = Column(Date)
    email = Column(String(255), index=True)
    password = Column(String(255), index=True)
    

    role_id = Column(Integer, ForeignKey('role_job.id'))
    role_job = relationship("Role_Job", back_populates="user_jobs")
