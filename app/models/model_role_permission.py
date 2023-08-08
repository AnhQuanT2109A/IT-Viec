from app.models.model_base import BareBaseModel
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
class Role_Permission(BareBaseModel):
    role_id = Column(Integer, ForeignKey('role_job.id'))
    role_job = relationship("Role_Job", back_populates="role_permissions")

    permission_id = Column(Integer, ForeignKey('permission_job.id'))
    permission_job = relationship("Permission_Job", back_populates="role_permissions")