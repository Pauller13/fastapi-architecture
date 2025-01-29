from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from utils.get_current_user import get_current_user
from utils.hash_password import hash_password
from schemas.users.user_response_schema import UserResponseSchema
from utils.get_session import get_session
from schemas.users.user_create_schema import UserCreateSchema
from models.user_model import UserModel as User
from utils.get_current_user import oauth2_scheme

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

@router.post("/create", response_model=UserResponseSchema)
def create_user(user: UserCreateSchema, session: Session = Depends(get_session)):
    # if current_user.role != "admin":
    #     raise HTTPException(status_code=403, detail="Vous devez avoir le role admin pour créer un utilisateur")
    
    # Vérifier si l'utilisateur existe déjà
    db_user = session.exec(select(User).where(User.username == user.username)).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    # Hacher le mot de passe
    hashed_password = hash_password(user.password)
    db_user = User(username=user.username, password=hashed_password, email=user.email)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    
    return db_user



@router.get("/me", response_model=UserResponseSchema)
def get_profil(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)):
    user = get_current_user(token, session)
    return user


