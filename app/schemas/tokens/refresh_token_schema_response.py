from sqlmodel import SQLModel
from datetime import datetime

class RefreshTokenResponseSchema(SQLModel):
    access_token: str
