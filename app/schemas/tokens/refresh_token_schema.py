from sqlmodel import SQLModel, Field
from datetime import datetime

class RefreshTokenSchema(SQLModel):
    refresh_token: str
