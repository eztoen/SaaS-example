
from sqlite3 import IntegrityError
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import HTTPException, status

from api.schemas.auth import RegisterSchema

from core.services import get_psw_hash, verify_psw
from core.models.users import Users

async def register(user_register: RegisterSchema, session: AsyncSession):
    select_stmt = select(Users).where(Users.email == user_register.email)
    result = await session.execute(select_stmt)
    user = result.scalar_one_or_none()
    
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='This account already exists'
        )
        
    user = Users(
        username = user_register.username,
        email = user_register.email,
        hashed_password = get_psw_hash(user_register.password)
    )
    session.add(user)
    
    try:
        await session.commit()
        
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='This username already exists'
        )
        
    else:
        return {'success': True}