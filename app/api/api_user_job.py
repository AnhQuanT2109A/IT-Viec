import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db
from app.helpers.exception_handler import CustomException

from app.helpers.paging import Page, PaginationParams, paginate
from app.models.model_user_job import User_Job
from app.schemas.sche_base import DataResponse
from app.schemas.sche_user_job import User_JobCreateRequest, User_JobRead, User_JobUpdateRequest
from app.services.srv_user_job import User_JobService
from sqlalchemy.orm import joinedload



logger = logging.getLogger()
router = APIRouter()

@router.get("", response_model=Page[User_JobRead])
def get(params: PaginationParams = Depends()) -> Any:
    """
    API Get list User_Job
    """
    try:
        _query = db.session.query(User_Job)
        user_jobs = paginate(model=User_Job, query=_query, params=params)
        return user_jobs
    except Exception as e:
        return HTTPException(status_code=400, detail=logger.error(e))

@router.post("")
def create(user_job_data: User_JobCreateRequest) -> Any:
    """
    API Create User_Job
    """
    try:
        exist_user_job = db.session.query(User_Job).filter(User_Job.email == user_job_data.email).first()
        if exist_user_job:
            raise Exception('Already exists')
        new_user_job = User_JobService().create_user_job(user_job_data)
        return DataResponse().success_response(data=new_user_job)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
    
@router.get("/{user_job_id}")
def detail(user_job_id: int) -> Any:
    """
    API get Detail User_Job
    """
    try:
        exist_user_job = db.session.query(User_Job).options(joinedload(User_Job.role_job)).get(user_job_id)
        if exist_user_job is None:
            raise Exception('User Job does not exist')
        return DataResponse().success_response(data=exist_user_job)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))

@router.put("/{user_job_id}")
def update(user_job_id: int, user_job_data: User_JobUpdateRequest) -> Any:
    """
    API update User_Job
    """
    try:
        exist_user_job = db.session.query(User_Job).get(user_job_id)
        if exist_user_job is None:
            raise Exception('User Job already exists')
        updated_user_job = User_JobService().update(user_job=exist_user_job, data=user_job_data)
        return DataResponse().success_response(data=updated_user_job)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
    
@router.delete("/{user_job_id}")
def delete(user_job_id: int) -> Any:
    """
    API delete User Job
    """
    try:
        exist_user_job = db.session.query(User_Job).filter(User_Job.id == user_job_id).first()
        if exist_user_job is None:
            raise Exception('This user job cannot be deleted')
        db.session.delete(exist_user_job)
        db.session.commit()
        return DataResponse().success_response(data=f"Role Job with ID {user_job_id} has been deleted.")

    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
 