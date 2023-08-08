from fastapi.security import HTTPBearer
from fastapi_sqlalchemy import db
from app.models.model_user_job import User_Job

from app.schemas.sche_user_job import User_JobCreateRequest, User_JobUpdateRequest


class User_JobService(object):
    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod
    def create_user_job(data: User_JobCreateRequest):
        new_user_job = User_Job(
            full_name = data.full_name,
            phone = data.phone,
            date_of_birth = data.date_of_birth,
            email = data.email,
            password = data.password,
            role_id = data.role_id
        )
        db.session.add(new_user_job)
        db.session.commit()
        return new_user_job
    
    @staticmethod
    def update(user_job: User_Job, data: User_JobUpdateRequest):
        user_job.full_name = user_job.full_name if data.full_name is None else data.full_name
        user_job.phone = user_job.phone if data.phone is None else data.phone
        user_job.date_of_birth = user_job.date_of_birth if data.date_of_birth is None else data.date_of_birth
        user_job.email = user_job.email if data.email is None else data.email
        user_job.password = user_job.password if data.password is None else data.password
        user_job.role_id = user_job.role_id if data.role_id is None else data.role_id
        
        db.session.commit()
        return user_job