import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db
from app.helpers.exception_handler import CustomException

from app.helpers.paging import Page, PaginationParams, paginate
from app.models.model_author import Author
from app.schemas.sche_author import AuthorCreateRequest, AuthorRead, AuthorUpdateRequest
from app.schemas.sche_base import DataResponse
from app.services.srv_author import AuthorService


logger = logging.getLogger()
router = APIRouter()

@router.get("", response_model=Page[AuthorRead])
def get(params: PaginationParams = Depends()) -> Any:
    """
    API Get list Author
    """
    try:
        _query = db.session.query(Author)
        authors = paginate(model=Author, query=_query, params=params)
        return authors
    except Exception as e:
        return HTTPException(status_code=400, detail=logger.error(e))
    
@router.post("", response_model=DataResponse[AuthorRead])
def create(author_data: AuthorCreateRequest) -> Any:
    """
    API Create Author
    """
    try:
        exist_email = db.session.query(Author).filter(Author.email == author_data.email).first()
        if exist_email:
            raise Exception('Email Author already exists')
        new_author = AuthorService().create_author(author_data)
        return DataResponse().success_response(data=new_author)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
    
@router.get("/{author_id}", response_model=DataResponse[AuthorRead])
def detail(author_id: int) -> Any:
    """
    API get Detail Author
    """
    try:
        exist_author = db.session.query(Author).get(author_id)
        if exist_author is None:
            raise Exception('Author already exists')
        return DataResponse().success_response(data=exist_author)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
    
@router.put("/{author_id}", response_model=DataResponse[AuthorRead])
def update(author_id: int, author_data: AuthorUpdateRequest) -> Any:
    """
    API update Author
    """
    try:
        exist_author = db.session.query(Author).get(author_id)
        if exist_author is None:
            raise Exception('Author already exists')
        updated_author = AuthorService().update_author(author=exist_author, data=author_data)
        return DataResponse().success_response(data=updated_author)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
    
@router.delete("/{author_id}")
def delete(author_id: int) -> Any:
    """
    API delete Author
    """
    try:
        exist_author = db.session.query(Author).filter(Author.id == author_id).first()
        if exist_author is None:
            raise Exception('This author cannot be deleted')
        db.session.delete(exist_author)
        db.session.commit()
        return DataResponse().success_response(data=f"Role Job with ID {author_id} has been deleted.")

    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
