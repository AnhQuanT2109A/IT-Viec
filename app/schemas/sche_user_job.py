
from datetime import date
from pydantic import BaseModel

from app.schemas.sche_role_job import Role_JobRead


class User_JobBase(BaseModel):
    full_name: str
    phone: str
    date_of_birth: date
    email: str
    password: str
    role_id: int

    class Config:
        orm_mode = True

class User_JobRead(User_JobBase):
    id: int
    Role_Job: Role_JobRead
    pass

class User_JobCreateRequest(User_JobBase):
    pass

class User_JobUpdateRequest(User_JobBase):
    pass