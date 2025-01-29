from sqlmodel import create_engine
from sqlmodel import Session
import os
from dotenv import load_dotenv

load_dotenv()


postgresql_url = os.getenv("DATABASE_URL")

engine = create_engine(postgresql_url)


def get_session():
    with Session(engine) as session:
        yield session