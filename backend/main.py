from datetime import datetime
from enum import Enum
from typing import List, Optional
from urllib.request import Request

from fastapi import FastAPI, Depends
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, ValidationError
from sqlalchemy import insert, delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.responses import JSONResponse

from crud import check_email
from database import get_async_session
from models.users import users
from schemes.schemes import User

app = FastAPI(
    title = "Test api"
)


@app.post("/")
async def add_specific_operations(new_user: User, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(users).values(**new_user.dict())
    if check_email(email = new_user.email):
        return {"status": "email already registred"}
    else:
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}


@app.delete("/{user_id}/")
async def add_specific_operations(user_id : int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(users).where(users.c.id == user_id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}