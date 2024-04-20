from .config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Adding Dependency
def get_db():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

db_gen = get_db()
db = next(db_gen)