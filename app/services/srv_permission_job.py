
from fastapi.security import HTTPBearer
from fastapi_sqlalchemy import db
from app.models.model_permission_job import Permission_Job

from app.schemas.sche_permission_job import Permission_JobCreateRequest, Permission_JobUpdateRequest


class Permission_JobService(object):
    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod
    def create_permission_job(data: Permission_JobCreateRequest):
        new_permission_job = Permission_Job(
            permission_name = data.permission_name,
        )
        db.session.add(new_permission_job)
        db.session.commit()
        return new_permission_job
    
    @staticmethod
    def update(permission_job: Permission_Job, data: Permission_JobUpdateRequest):
        permission_job.permission_name = permission_job.permission_name if data.permission_name is None else data.permission_name
        db.session.commit()
        return permission_job