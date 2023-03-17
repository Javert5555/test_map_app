from dataclasses import Field

from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(
    prefix = "/users",
    tags = ["Users"]
)

@router.post("/")
async def get_operations():
    return {"messege, hi"}