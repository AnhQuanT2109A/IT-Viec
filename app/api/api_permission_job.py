import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db
from app.helpers.exception_handler import CustomException

from app.helpers.paging import Page, PaginationParams, paginate
from app.models.model_permission_job import Permission_Job
from app.schemas.sche_base import DataResponse
from app.schemas.sche_permission_job import Permission_JobCreateRequest, Permission_JobRead, Permission_JobUpdateRequest
from app.services.srv_permission_job import Permission_JobService


logger = logging.getLogger()
router = APIRouter()

@router.get("", response_model=Page[Permission_JobRead])
def get(params: PaginationParams = Depends()) -> Any:
    """
    API Get list Permission_Job
    """
    try:
        _query = db.session.query(Permission_Job)
        products = paginate(model=Permission_Job, query=_query, params=params)
        return products
    except Exception as e:
        return HTTPException(status_code=400, detail=logger.error(e))
    
@router.post("", response_model=DataResponse[Permission_JobRead])
def create(permission_job_data: Permission_JobCreateRequest) -> Any:
    """
    API Create Permission_Job
    """
    try:
        exist_permission_job = db.session.query(Permission_Job).filter(Permission_Job.permission_name == permission_job_data.permission_name).first()
        if exist_permission_job:
            raise Exception('Permission Name already exists')
        new_role_job = Permission_JobService().create_permission_job(permission_job_data)
        return DataResponse().success_response(data=new_role_job)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
    
@router.get("/{permission_job_id}", response_model=DataResponse[Permission_JobRead])
def detail(permission_job_id: int) -> Any:
    """
    API get Detail Permission_Job
    """
    try:
        exist_permission_job = db.session.query(Permission_Job).get(permission_job_id)
        if exist_permission_job is None:
            raise Exception('Permission Job already exists')
        return DataResponse().success_response(data=exist_permission_job)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
    
@router.put("/{permission_job_id}", response_model=DataResponse[Permission_JobRead])
def update(permission_job_id: int, permission_job_data: Permission_JobUpdateRequest) -> Any:
    """
    API update Permission_Job
    """
    try:
        exist_permission_job = db.session.query(Permission_Job).get(permission_job_id)
        if exist_permission_job is None:
            raise Exception('Permission Job already exists')
        updated_permission_job = Permission_JobService().update(permission_job=exist_permission_job, data=permission_job_data)
        return DataResponse().success_response(data=updated_permission_job)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
    
@router.delete("/{permission_job_id}")
def delete(permission_job_id: int) -> Any:
    """
    API delete Permission_Job
    """
    try:
        exist_permission_job = db.session.query(Permission_Job).filter(Permission_Job.id == permission_job_id).first()
        if exist_permission_job is None:
            raise Exception('This permission job cannot be deleted')
        db.session.delete(exist_permission_job)
        db.session.commit()
        return DataResponse().success_response(data=f"Role Job with ID {permission_job_id} has been deleted.")

    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))