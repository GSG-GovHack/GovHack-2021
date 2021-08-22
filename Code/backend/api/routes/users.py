from fastapi import APIRouter

from api.models import User, UserIn

router = APIRouter(prefix='users/')

@router.post('/')
async def create_user(user: UserIn):
    pass