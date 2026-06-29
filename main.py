from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(
    title='Xử lý đăng ký học viên',
    description='Xử lý đăng ký học viên với Request Body',
    version='1.0.0'
)

class StudentRegister(BaseModel):
    full_name: str = Field(..., min_length=3)
    email: EmailStr
    age: int = Field(..., ge=15, le=60)
    phone: str = Field(..., pattern=r"^\d{10,11}$")
    course: str
    note: Optional[str] = Field(default=None, max_length=200)
    
@app.post("/students/register")
def register_student(student: StudentRegister):
    data = student.model_dump()
    
    data["full_name"] = data["full_name"].strip().title()
    
    if data["note"]:
        data["note"] = data["note"].strip().lower()
        
    return {
        "message": "Đăng ký học viên thành công",
        "data": data       
    }
