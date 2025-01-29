from sqlmodel import SQLModel, Field
from datetime import datetime

class AccessTokenSchema(SQLModel):
    access_token: str
    refresh_token: str
    token_type: str