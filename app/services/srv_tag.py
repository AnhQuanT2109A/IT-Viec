

from fastapi.security import HTTPBearer
from fastapi_sqlalchemy import db

from app.models.model_tag import Tag
from app.schemas.sche_tag import TagCreateRequest, TagUpdateRequest


class TagService(object):
    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod
    def create_tag(data: TagCreateRequest):
        new_tag = Tag(
            tag_name = data.tag_name
        )
        db.session.add(new_tag)
        db.session.commit()
        return new_tag
    
    @staticmethod
    def update_tag(tag: Tag, data: TagUpdateRequest):
        tag.tag_name = tag.tag_name if data.tag_name is None else data.tag_name
        
        db.session.commit()
        return tag