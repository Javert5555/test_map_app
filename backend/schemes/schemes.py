from pydantic import BaseModel, Field ,EmailStr


class User(BaseModel):
    email : EmailStr
    username : str = Field(min_length=5)
    password : str = Field(min_length = 5)