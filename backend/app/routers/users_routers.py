from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..services.user_services import UserServices
from ..schemas.user import UserResponse, UserCreate


router = APIRouter(
    prefix="/api/users",
    tags=["users"]
)

@router.get("/get_users", response_model=List[UserResponse], status_code=status.HTTP_200_OK)
def get_all_users(db: Session=Depends(get_db)):
    services = UserServices(db)
    return services.get_all_users()

@router.get("/get_users/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_user(user_id: int, db: Session=Depends(get_db)):
    services = UserServices(db)
    return services.get_by_id(user_id)

@router.post("/create_user", response_model=UserResponse, status_code=status.HTTP_200_OK)
def create_user(user_data: UserCreate, db: Session=Depends(get_db)):
    services = UserServices(db)
    return services.create(user_data)