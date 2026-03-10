from sqlalchemy import Column, Integer, String

from .database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), nullable=False, index=True)
    age = Column(Integer, nullable=False)
    gender = Column(String(10), nullable=False)
    student_no = Column(String(20), unique=True, nullable=False, index=True)
    major = Column(String(100), nullable=True)

