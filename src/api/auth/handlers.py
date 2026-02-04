from fastapi import APIRouter, Depends, Request

from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from core.db_helper import get_db
from api.schemas.auth import RegisterSchema

router = APIRouter(tags=['Account'])

@router.post('/register')
async def register(
    request: Request,
    user_register: RegisterSchema,
    session: AsyncSession = Depends(get_db)
):
    return await crud.register(
        user_register=user_register,
        session=session
    )