from pydantic import BaseModel, Field, field_validator
import uuid
from datetime import datetime

class UserCreateModel(BaseModel):
    first_name: str = Field(max_length=25)
    last_name: str = Field(max_length=25)
    username: str = Field(max_length=15)
    email: str = Field(max_length=40)
    # allow up to bcrypt's byte-limit; we also validate later
    password: str = Field(max_length=72)

    # ensure length in bytes does not exceed bcrypt limit (72 bytes)
    @field_validator("password")
    def password_byte_length(cls, v: str) -> str:
        if len(v.encode("utf-8")) > 72:
            raise ValueError("password must be 72 bytes or fewer (bcrypt limit)")
        return v


class UserModel(BaseModel):
    uid: uuid.UUID
    username: str
    email: str
    first_name: str
    last_name: str
    password_hash:str= Field(exclude=True)
    is_verified: bool = False

    created_at: datetime 

    updated_at: datetime 
class UserLoginModel(BaseModel):
    email:str=Field(max_length=40)
    password:str=Field(min_length=8)
    