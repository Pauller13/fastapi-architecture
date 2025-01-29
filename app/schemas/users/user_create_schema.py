from sqlmodel import SQLModel


class UserCreateSchema(SQLModel):
    username: str
    password: str
    email: str