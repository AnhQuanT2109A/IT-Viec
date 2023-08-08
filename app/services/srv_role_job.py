from fastapi.security import HTTPBearer
from fastapi_sqlalchemy import db

from app.models.model_role_job import Role_Job
from app.schemas.sche_role_job import Role_JobCreateRequest, Role_JobUpdateRequest


class Role_JobService(object):
    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod
    def create_role_job(data: Role_JobCreateRequest):
        new_role_job = Role_Job(
            role_name = data.role_name,
        )
        db.session.add(new_role_job)
        db.session.commit()
        return new_role_job
    
    @staticmethod
    def update(role_job: Role_Job, data: Role_JobUpdateRequest):
        role_job.role_name = role_job.role_name if data.role_name is None else data.role_name
        db.session.commit()
        return role_job