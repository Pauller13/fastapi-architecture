from typing import Optional
from sqlmodel import Field


class UserMixin:
    created_by: Optional[str] = Field(default=None)
    updated_by: Optional[str] = Field(default=None)