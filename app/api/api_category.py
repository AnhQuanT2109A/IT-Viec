import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db
from app.helpers.exception_handler import CustomException

from app.helpers.paging import Page, PaginationParams, paginate
from app.models.model_category import Category
from app.schemas.sche_base import DataResponse
from app.schemas.sche_category import CategoryCreateRequest, CategoryRead, CategoryUpdateRequest
from app.services.srv_category import CategoryService


logger = logging.getLogger()
router = APIRouter()

@router.get("", response_model=Page[CategoryRead])
def get(params: PaginationParams = Depends()) -> Any:
    """
    API Get list Category
    """
    try:
        _query = db.session.query(Category)
        products = paginate(model=Category, query=_query, params=params)
        return products
    except Exception as e:
        return HTTPException(status_code=400, detail=logger.error(e))
    
@router.post("", response_model=DataResponse[CategoryRead])
def create(category_data: CategoryCreateRequest) -> Any:
    """
    API Create Category
    """
    try:
        exist_category = db.session.query(Category).filter(Category.category_name == category_data.category_name).first()
        if exist_category:
            raise Exception('Category Name already exists')
        new_category = CategoryService().create_category(category_data)
        return DataResponse().success_response(data=new_category)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
    
@router.get("/{category_id}", response_model=DataResponse[CategoryRead])
def detail(category_id: int) -> Any:
    """
    API get Detail Category
    """
    try:
        exist_category = db.session.query(Category).get(category_id)
        if exist_category is None:
            raise Exception('Directory does not exist')
        return DataResponse().success_response(data=exist_category)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
    
@router.put("/{category_id}", response_model=DataResponse[CategoryRead])
def update(category_id: int, category_data: CategoryUpdateRequest) -> Any:
    """
    API update Category
    """
    try:
        exist_category = db.session.query(Category).get(category_id)
        if exist_category is None:
            raise Exception('Category already exists')
        updated_category = CategoryService().update_category(category=exist_category, data=category_data)
        return DataResponse().success_response(data=updated_category)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
    
@router.delete("/{category_id}")
def delete(category_id: int) -> Any:
    """
    API delete Category
    """
    try:
        exist_category = db.session.query(Category).filter(Category.id == category_id).first()
        if exist_category is None:
            raise Exception('This category cannot be deleted')
        db.session.delete(exist_category)
        db.session.commit()
        return DataResponse().success_response(data=f"Category with ID {category_id} has been deleted.")

    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))

