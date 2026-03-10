from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# 根据你的本地 MySQL 环境修改：
# 例如：mysql+pymysql://root:123456@localhost:3306/student_db
DATABASE_URL = "mysql+pymysql://root:921405b921405B@localhost:3306/student_db"

engine = create_engine(
    DATABASE_URL,
    echo=False,
    future=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

