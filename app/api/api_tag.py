import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db
from app.helpers.exception_handler import CustomException

from app.helpers.paging import Page, PaginationParams, paginate
from app.models.model_tag import Tag
from app.schemas.sche_base import DataResponse
from app.schemas.sche_tag import TagCreateRequest, TagRead, TagUpdateRequest
from app.services.srv_tag import TagService


logger = logging.getLogger()
router = APIRouter()

@router.get("", response_model=Page[TagRead])
def get(params: PaginationParams = Depends()) -> Any:
    """
    API Get list Tag
    """
    try:
        _query = db.session.query(Tag)
        tags = paginate(model=Tag, query=_query, params=params)
        return tags
    except Exception as e:
        return HTTPException(status_code=400, detail=logger.error(e))
    
@router.post("", response_model=DataResponse[TagRead])
def create(tag_data: TagCreateRequest) -> Any:
    """
    API Create Tag
    """
    try:
        exist_tag = db.session.query(Tag).filter(Tag.tag_name == tag_data.tag_name).first()
        if exist_tag:
            raise Exception('Tag Name already exists')
        new_tag = TagService().create_tag(tag_data)
        return DataResponse().success_response(data=new_tag)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
    
@router.get("/{tag_id}", response_model=DataResponse[TagRead])
def detail(tag_id: int) -> Any:
    """
    API get Detail Tag
    """
    try:
        exist_tag = db.session.query(Tag).get(tag_id)
        if exist_tag is None:
            raise Exception('Tag already exists')
        return DataResponse().success_response(data=exist_tag)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
    
@router.put("/{tag_id}", response_model=DataResponse[TagRead])
def update(tag_id: int, tag_data: TagUpdateRequest) -> Any:
    """
    API update Role_Job
    """
    try:
        exist_tag = db.session.query(Tag).get(tag_id)
        if exist_tag is None:
            raise Exception('Tag already exists')
        updated_tag = TagService().update_tag(tag=exist_tag, data=tag_data)
        return DataResponse().success_response(data=updated_tag)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
    
@router.delete("/{tag_id}")
def delete(tag_id: int) -> Any:
    """
    API delete Tag
    """
    try:
        exist_tag = db.session.query(Tag).filter(Tag.id == tag_id).first()
        if exist_tag is None:
            raise Exception('This tag cannot be deleted')
        db.session.delete(exist_tag)
        db.session.commit()
        return DataResponse().success_response(data=f"Role Job with ID {tag_id} has been deleted.")

    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))

