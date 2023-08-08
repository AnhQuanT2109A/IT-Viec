from app.models.model_base import BareBaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Role_Job(BareBaseModel):
    role_name = Column(String)

    user_jobs = relationship("User_Job", back_populates="role_job")
    role_permissions = relationship("Role_Permission", back_populates="role_job")
