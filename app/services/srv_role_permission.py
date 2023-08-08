from fastapi.security import HTTPBearer
from fastapi_sqlalchemy import db
from app.models.model_permission_job import Permission_Job
from app.models.model_role_permission import Role_Permission

from app.schemas.sche_role_permission import Role_PermissionCreateRequest, Role_PermissionUpdateRequest


class Role_PermisionService(object):
    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod
    def create_role_permission(data: Role_PermissionCreateRequest):
        new_role_permission = Role_Permission(
            role_id = data.role_id,
            permission_id = data.permission_id
        )
        db.session.add(new_role_permission)
        db.session.commit()
        return new_role_permission
    
    @staticmethod
    def update(role_permission: Role_Permission, data: Role_PermissionUpdateRequest):
        role_permission.role_id = role_permission.role_id if data.role_id is None else data.role_id
        role_permission.permission_id = role_permission.permission_id if data.permission_id is None else data.permission_id
        db.session.commit()
        return role_permission
