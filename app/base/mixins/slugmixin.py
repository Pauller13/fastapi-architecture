from sqlmodel import Field
import uuid


class SlugMixin:
    slug = Field(default_factory=lambda: str(uuid.uuid4()))