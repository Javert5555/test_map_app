from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON

metadata = MetaData()


users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True,  autoincrement=True),
    Column("email", String, unique=True),
    Column("username", String, nullable=False, unique=True),
    Column("password", String, nullable=False)
)



