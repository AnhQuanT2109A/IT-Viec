
from pydantic import BaseModel
from app.schemas.sche_permission_job import Permission_JobRead

from app.schemas.sche_role_job import Role_JobRead




class Role_PermissionBase(BaseModel):
    permission_id: int
    role_id: int

    class Config:
        orm_mode = True

class Role_PermissionRead(Role_PermissionBase):
    id: int
    Role_Job: Role_JobRead
    Permission_Job: Permission_JobRead
    pass

class Role_PermissionCreateRequest(Role_PermissionBase):
    pass

class Role_PermissionUpdateRequest(Role_PermissionBase):
    pass