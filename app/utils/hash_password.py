from utils.config import pwd_context


def hash_password(password: str) -> str:
    return pwd_context.hash(password)