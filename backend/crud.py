from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from models.users import users
from schemes.schemes import User


def check_email(email:str, session: AsyncSession = Depends(get_async_session)):
    t = select(users).where(users.c.email == email)
    return session.execute(t)