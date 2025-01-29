from sqlmodel import SQLModel


class TokenData(SQLModel):
    username: str