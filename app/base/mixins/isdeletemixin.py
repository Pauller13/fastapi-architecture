from sqlmodel import Field
from datetime import datetime


class IsDeleteMixin:
    is_delete = Field(default=False)
    deleted_at = Field(default_factory=datetime.utcnow)