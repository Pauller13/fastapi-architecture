from sqlmodel import SQLModel

class UserUpdateSchema(SQLModel):
    username: str
    email: str