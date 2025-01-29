from base.mixins.isdeletemixin import IsDeleteMixin
from base.mixins.slugmixin import SlugMixin
from base.mixins.timestamp import TimestampMixin
from sqlmodel import SQLModel, Field


class ModelWithoutUserMixin(SQLModel, TimestampMixin, SlugMixin, IsDeleteMixin):
    id : int = Field(default=None, primary_key=True)