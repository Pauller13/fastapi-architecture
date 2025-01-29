from sqlmodel import SQLModel
from datetime import datetime


class UserResponseSchema(SQLModel):
    id: int 
    username: str 
    email: str 
    created_at: datetime 
    updated_at: datetime 