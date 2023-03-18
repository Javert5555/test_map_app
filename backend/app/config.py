import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_PORT: int = os.getenv('DATABASE_PORT')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_DB: str = os.getenv('POSTGRES_DB')
    POSTGRES_HOST: str = os.getenv('POSTGRES_HOST')
#     POSTGRES_HOSTNAME: str

class Config:
    env_file = './.env'

settings:Settings = Settings()



db_host = os.getenv('DB_HOST',default="localhost")
jwt_secret = "secret"
jwt_algorithm = "HS256"