from fastapi.security import HTTPBearer
from fastapi_sqlalchemy import db
from app.models.model_author import Author

from app.schemas.sche_author import AuthorCreateRequest, AuthorUpdateRequest



class AuthorService(object):
    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod
    def create_author(data: AuthorCreateRequest):
        new_author = Author(
            full_name = data.full_name,
            email = data.email,
            bio = data.bio
        )
        db.session.add(new_author)
        db.session.commit()
        return new_author
    
    @staticmethod
    def update_author(author: Author, data: AuthorUpdateRequest):
        author.full_name = author.full_name if data.full_name is None else data.full_name
        author.email = author.email if data.email is None else data.email
        author.bio = author.bio if data.bio is None else data.bio
        db.session.commit()
        return author