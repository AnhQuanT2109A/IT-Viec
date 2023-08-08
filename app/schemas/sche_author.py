from pydantic import BaseModel


class AuthorBase(BaseModel):
    full_name: str
    email: str
    bio: str

    class Config:
        orm_mode = True

class AuthorRead(AuthorBase):
    id: int
    pass

class AuthorCreateRequest(AuthorBase):
    pass

class AuthorUpdateRequest(AuthorBase):
    pass