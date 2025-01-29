from sqlmodel import Field
from datetime import datetime


class TimestampMixin:
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow,sa_column_kwargs={'onupdate': datetime.utcnow})