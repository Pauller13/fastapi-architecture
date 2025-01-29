from base.mixins.isdeletemixin import IsDeleteMixin
from base.mixins.slugmixin import SlugMixin
from base.mixins.timestamp import TimestampMixin
from base.mixins.usermixin import UserMixin
from sqlmodel import SQLModel, Field


class ModelWithAllMixin(SQLModel, IsDeleteMixin, TimestampMixin, SlugMixin, UserMixin):
    id: int = Field(default=None, primary_key=True)