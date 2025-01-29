from sqlmodel import Field
from base.helpers.model_with_all_mixin import ModelWithAllMixin

class UserModel(ModelWithAllMixin, table=True):
    username: str
    password: str
    email: str