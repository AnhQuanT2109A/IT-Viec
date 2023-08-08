from app.models.model_base import BareBaseModel
from sqlalchemy import Column, String


class Author(BareBaseModel):
    full_name = Column(String, index=True)
    email = Column(String, index=True)
    bio = Column(String)