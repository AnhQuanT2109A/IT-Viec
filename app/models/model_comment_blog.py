from app.models.model_base import BareBaseModel
from sqlalchemy import Column, String

class Comment_Blog(BareBaseModel):
    commenter_name = Column(String)
    commenter_text = Column(String)
