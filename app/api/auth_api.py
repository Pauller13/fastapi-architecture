import os
import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from models.user_model import UserModel
from schemas.tokens.refresh_token_schema_response import RefreshTokenResponseSchema
from schemas.users.user_login_schema import UserLoginSchema
from utils.get_session import get_session
from utils.verify_password import verify_password
from utils.create_acces_token import create_access_token
from utils.create_refresh_token import create_refresh_token
from schemas.tokens.acces_token_schema import AccessTokenSchema
from schemas.tokens.refresh_token_schema import RefreshTokenSchema
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.post("/token", response_model=AccessTokenSchema)
def login_for_access_token(form_data: UserLoginSchema, session: Session = Depends(get_session)):
    db_user = session.exec(select(UserModel).where(UserModel.username == form_data.username)).first()
    if db_user is None or not verify_password(form_data.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        ) 
    
    access_token = create_access_token(data={"username": db_user.username})
    refresh_token = create_refresh_token(data={"username": db_user.username})
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

@router.post("/refresh-token", response_model=RefreshTokenResponseSchema)
def refresh_access_token(refresh_token: RefreshTokenSchema, session: Session = Depends(get_session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate refresh token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(refresh_token.refresh_token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")])
        username: str = payload.get("username")
        if username is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception

    db_user = session.exec(select(UserModel).where(UserModel.username == username)).first()
    if db_user is None:
        raise credentials_exception

    access_token = create_access_token(data={"username": db_user.username})
    return {"access_token": access_token}