
import logging
from typing import Any
from fastapi import APIRouter, Depends, HTTPException

from fastapi_sqlalchemy import db
from app.helpers.exception_handler import CustomException

from app.helpers.paging import Page, PaginationParams, paginate
from app.models.model_role_job import Role_Job
from app.schemas.sche_base import DataResponse
from app.schemas.sche_role_job import Role_JobCreateRequest, Role_JobRead, Role_JobUpdateRequest
from app.services.srv_role_job import Role_JobService
logger = logging.getLogger()
router = APIRouter()

@router.get("", response_model=Page[Role_JobRead])
def get(params: PaginationParams = Depends()) -> Any:
    """
    API Get list Role_Job
    """
    try:
        _query = db.session.query(Role_Job)
        products = paginate(model=Role_Job, query=_query, params=params)
        return products
    except Exception as e:
        return HTTPException(status_code=400, detail=logger.error(e))
    
@router.post("", response_model=DataResponse[Role_JobRead])
def create(role_job_data: Role_JobCreateRequest) -> Any:
    """
    API Create Role_Job
    """
    try:
        exist_role_job = db.session.query(Role_Job).filter(Role_Job.role_name == role_job_data.role_name).first()
        if exist_role_job:
            raise Exception('Role Name already exists')
        new_role_job = Role_JobService().create_role_job(role_job_data)
        return DataResponse().success_response(data=new_role_job)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
    
@router.get("/{role_job_id}", response_model=DataResponse[Role_JobRead])
def detail(role_job_id: int) -> Any:
    """
    API get Detail Role_Job
    """
    try:
        exist_role_job = db.session.query(Role_Job).get(role_job_id)
        if exist_role_job is None:
            raise Exception('Role Job already exists')
        return DataResponse().success_response(data=exist_role_job)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
    
@router.put("/{role_job_id}", response_model=DataResponse[Role_JobRead])
def update(role_job_id: int, role_job_data: Role_JobUpdateRequest) -> Any:
    """
    API update Role_Job
    """
    try:
        exist_role_job = db.session.query(Role_Job).get(role_job_id)
        if exist_role_job is None:
            raise Exception('Role Job already exists')
        updated_role_job = Role_JobService().update(role_job=exist_role_job, data=role_job_data)
        return DataResponse().success_response(data=updated_role_job)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
    
@router.delete("/{role_job_id}")
def delete(role_job_id: int) -> Any:
    """
    API delete Role_Job
    """
    try:
        exist_role_job = db.session.query(Role_Job).filter(Role_Job.id == role_job_id).first()
        if exist_role_job is None:
            raise Exception('This role job cannot be deleted')
        db.session.delete(exist_role_job)
        db.session.commit()
        return DataResponse().success_response(data=f"Role Job with ID {role_job_id} has been deleted.")

    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))

