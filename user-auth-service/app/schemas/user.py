from pydantic import BaseModel

class UserCreate(BaseModel):
    user_name: str
    password: str

class UserLogin(BaseModel):
    user_name: str
    password: str

class UserResponse(BaseModel):
    user_id: int
    user_name: str
    token: str