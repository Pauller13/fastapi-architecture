from fastapi import FastAPI
from api.auth_api import router as auth_router
from api.user_api import router as user_router
app = FastAPI()
app.include_router(auth_router)
app.include_router(user_router)