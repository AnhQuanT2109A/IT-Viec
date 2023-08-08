from pydantic import BaseModel


class TagBase(BaseModel):
    tag_name: str

    class Config:
        orm_mode = True

class TagRead(TagBase):
    id: int
    pass

class TagCreateRequest(TagBase):
    pass

class TagUpdateRequest(TagBase):
    pass