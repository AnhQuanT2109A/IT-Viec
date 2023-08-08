from pydantic import BaseModel


class CategoryBase(BaseModel):
    category_name: str

    class Config:
        orm_mode = True

class CategoryRead(CategoryBase):
    id: int
    pass

class CategoryCreateRequest(CategoryBase):
    pass

class CategoryUpdateRequest(CategoryBase):
    pass