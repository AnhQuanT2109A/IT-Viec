from fastapi.security import HTTPBearer
from fastapi_sqlalchemy import db
from app.models.model_category import Category

from app.schemas.sche_category import CategoryCreateRequest, CategoryUpdateRequest


class CategoryService(object):
    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod
    def create_category(data: CategoryCreateRequest):
        new_category = Category(
            category_name = data.category_name,
        )
        db.session.add(new_category)
        db.session.commit()
        return new_category
    
    @staticmethod
    def update_category(category: Category, data: CategoryUpdateRequest):
        category.category_name = category.category_name if data.category_name is None else data.category_name
        db.session.commit()
        return category