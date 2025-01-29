from sqlmodel import SQLModel


class UserLoginSchema(SQLModel):
    username: str
    password: str