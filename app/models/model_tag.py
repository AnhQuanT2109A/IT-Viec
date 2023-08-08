from app.models.model_base import BareBaseModel
from sqlalchemy import Column, String

class Tag(BareBaseModel):
    tag_name = Column(String, index=True)