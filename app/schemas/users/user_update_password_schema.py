from sqlmodel import SQLModel


class UserUpdatePasswordSchema(SQLModel):
    password: str
    new_password: str