from app.models.model_base import BareBaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Permission_Job(BareBaseModel):
    permission_name = Column(String)

    role_permissions = relationship("Role_Permission", back_populates="permission_job")
