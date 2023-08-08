

from pydantic import BaseModel


class Permission_JobBase(BaseModel):
    permission_name: str

    class Config:
        orm_mode = True

class Permission_JobRead(Permission_JobBase):
    id: int
    pass

class Permission_JobCreateRequest(Permission_JobBase):
    pass

class Permission_JobUpdateRequest(Permission_JobBase):
    pass