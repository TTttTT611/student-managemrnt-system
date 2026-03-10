from pydantic import BaseModel


class StudentBase(BaseModel):
    name: str
    age: int
    gender: str
    student_no: str
    major: str | None = None


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    gender: str | None = None
    major: str | None = None
    student_no: str | None = None 


class StudentOut(StudentBase):
    id: int

    class Config:
        orm_mode = True

