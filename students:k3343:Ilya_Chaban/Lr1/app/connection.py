import os
from sqlmodel import SQLModel, Session, create_engine
from dotenv import load_dotenv

load_dotenv()
db_url = os.getenv("DB_ADMIN")
if not db_url:
    raise ValueError("Переменная окружения DB_ADMIN не задана")

engine = create_engine(db_url, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session