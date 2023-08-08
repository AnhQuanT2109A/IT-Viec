from pydantic import BaseModel


class Comment_BlogBase(BaseModel):
    commenter_name: str
    comment_text: str

    class Config:
        orm_mode = True

class Comment_BlogRead(Comment_BlogBase):
    id: int
    pass

class Comment_BlogCreateRequest(Comment_BlogBase):
    pass

class Comment_BlogUpdateRequest(Comment_BlogBase):
    id: int
    pass