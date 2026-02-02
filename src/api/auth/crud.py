from sqlalchemy import select

from fastapi import HTTPException, status

from schemas.auth import RegisterSchema, LoginSchema

async def register():
    ...