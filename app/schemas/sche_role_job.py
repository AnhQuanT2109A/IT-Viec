
from pydantic import BaseModel


class Role_JobBase(BaseModel):
    role_name: str
    
    class Config:
        orm_mode = True

class Role_JobRead(Role_JobBase):
    id: int
    pass

class Role_JobCreateRequest(Role_JobBase):
    pass

class Role_JobUpdateRequest(Role_JobBase):
    pass