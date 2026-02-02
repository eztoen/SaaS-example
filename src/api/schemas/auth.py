import re

from pydantic import (
    BaseModel, 
    EmailStr, 
    Field, 
    field_validator
)

class Register(BaseModel):
    username: str = Field(..., min_length=5, max_length=30, pattern=r'^[a-zA-Z0-9_]+$')
    email: EmailStr = Field(..., max_length=255)
    password: str = Field(..., min_length=8, max_length=128)
    
    @field_validator('password')
    def validate_password(cls, value):
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter.")
        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter.")
        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one digit.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("Password must contain at least one special character.")
        if " " in value:
            raise ValueError("Password cannot contain spaces.")
        return value
    
class Login(BaseModel):
    email: EmailStr = Field(..., max_length=255)
    password: str = Field(..., min_length=8, max_length=128)