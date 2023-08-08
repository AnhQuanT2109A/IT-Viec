from fastapi import APIRouter
router = APIRouter()

from app.api import api_role_job, api_permission_job, api_role_permission, api_user_job, api_category, api_tag, api_author

router.include_router(api_role_job.router, tags=["role_job"], prefix="/role_job")
router.include_router(api_permission_job.router, tags=["permission_job"], prefix="/permission_job")
router.include_router(api_user_job.router, tags=["user_job"], prefix="/user_job")
router.include_router(api_role_permission.router, tags=["role_permission"], prefix="/role_permission")
router.include_router(api_category.router, tags=["category"], prefix="/category")
router.include_router(api_tag.router, tags=["tag"], prefix="/tag")
router.include_router(api_author.router, tags=["author"], prefix="/author")



