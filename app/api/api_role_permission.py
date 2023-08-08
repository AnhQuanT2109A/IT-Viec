
import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db
from app.helpers.exception_handler import CustomException
from app.helpers.paging import Page, PaginationParams, paginate
from app.models.model_role_permission import Role_Permission
from app.schemas.sche_base import DataResponse

from app.schemas.sche_role_permission import Role_PermissionCreateRequest, Role_PermissionRead, Role_PermissionUpdateRequest
from app.services.srv_role_permission import Role_PermisionService
from sqlalchemy.orm import joinedload



logger = logging.getLogger()
router = APIRouter()

@router.get("", response_model=Page[Role_PermissionRead])
def get(params: PaginationParams = Depends()) -> Any:
    """
    API Get list Role_permission
    """
    try:
        _query = db.session.query(Role_Permission)
        role_permissions = paginate(model=Role_Permission, query=_query, params=params)
        return role_permissions
    except Exception as e:
        return HTTPException(status_code=400, detail=logger.error(e))

@router.post("")
def create(role_permission_data: Role_PermissionCreateRequest) -> Any:
    """
    API Create Role Permission
    """
    try:
        new_role_permission = Role_PermisionService().create_role_permission(role_permission_data)
        return DataResponse().success_response(data=new_role_permission)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
    
@router.get("/{role_permission_id}")
def detail(role_permission_id: int) -> Any:
    """
    API get Detail Role Permission
    """
    try:
        exist_role_permission = db.session.query(Role_Permission).options(joinedload(Role_Permission.role_job and Role_Permission.permission_job)).get(role_permission_id)

        if exist_role_permission is None:
            raise Exception('Role Permission Job does not exist')
        return DataResponse().success_response(data=exist_role_permission)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))

@router.put("/{role_permission_id}")
def update(role_permission_id: int, role_permission_data: Role_PermissionUpdateRequest) -> Any:
    """
    API update Role Permission
    """
    try:
        exist_role_permission = db.session.query(Role_Permission).get(role_permission_id)
        if exist_role_permission is None:
            raise Exception('Role Permission already exists')
        updated_role_permission = Role_PermisionService().update(role_permission=exist_role_permission, data=role_permission_data)
        return DataResponse().success_response(data=updated_role_permission)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
    
@router.delete("/{role_permission_id}")
def delete(role_permission_id: int) -> Any:
    """
    API delete Role Permission
    """
    try:
        exist_role_permission = db.session.query(Role_Permission).filter(Role_Permission.id == role_permission_id).first()
        if exist_role_permission is None:
            raise Exception('This role permission cannot be deleted')
        db.session.delete(exist_role_permission)
        db.session.commit()
        return DataResponse().success_response(data=f"Role Job with ID {role_permission_id} has been deleted.")

    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))