from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLITE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLITE_URL,
    connect_args={"check_same_thread": False},
)

# обрабатывает запросы в базу данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()  # Базовый класс для всех будущих моделей


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    Base.metadata.create_all(bind=engine)
