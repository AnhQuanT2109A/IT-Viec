

from app.models.model_base import BareBaseModel
from sqlalchemy import Column, String


class Category(BareBaseModel):
    category_name = Column(String, index=True)

