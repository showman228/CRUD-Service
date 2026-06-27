from pydantic import BaseModel
from typing import List

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    pass

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True


class UserListResponse(BaseModel):
    users: List[UserResponse]