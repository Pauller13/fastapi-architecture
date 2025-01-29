from datetime import timedelta
import jwt
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


def create_access_token(data: dict, expires_delta: timedelta = timedelta(days=int(os.getenv("ACCESS_TOKEN_EXPIRE_DAYS")))) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
    return encoded_jwt