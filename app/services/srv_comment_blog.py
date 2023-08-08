from fastapi.security import HTTPBearer
from fastapi_sqlalchemy import db
from app.models.model_comment_blog import Comment_Blog

from app.schemas.sche_comment_blog import Comment_BlogCreateRequest, Comment_BlogUpdateRequest


class Comment_BlogService(object):
    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod
    def create_comment_blog(data: Comment_BlogCreateRequest):
        new_comment_blog = Comment_Blog(
            commenter_name = data.commenter_name,
            comment_text = data.comment_text
        )
        db.session.add(new_comment_blog)
        db.session.commit()
        return new_comment_blog
    
    @staticmethod
    def update_comment_blog(comment_blog: Comment_Blog, data: Comment_BlogUpdateRequest):
        comment_blog.commenter_name = comment_blog.commenter_name if data.commenter_name is None else data.commenter_name
        comment_blog.commenter_text = comment_blog.commenter_text if data.comment_text is None else data.comment_text

        db.session.commit()
        return comment_blog