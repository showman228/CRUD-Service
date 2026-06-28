from sqlalchemy.orm import Session
from backend.app.schemas.user import UserResponse, UserCreate
from backend.app.repository.user_repository import UserRepository
from fastapi import HTTPException, status
from typing import List


class UserServices:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def get_all_users(self) -> List[UserResponse]:
        users = self.repository.get_all()
        return [UserResponse.model_validate(u) for u in users]

    def get_by_id(self, user_id: int) -> UserResponse:
        user = self.repository.get_by_id(user_id)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with this id: {user_id} not found"
            )
        return UserResponse.model_validate(user)

    def get_by_username(self, username: str) -> UserResponse:
        user = self.repository.get_by_username(username)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"user with this username: {username} not found"
            )
        return UserResponse.model_validate(user)

    def get_by_email(self, user_email: str) -> UserResponse:
        user = self.repository.get_by_email(user_email)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"user with this user_email: {user_email} not found"
            )
        return UserResponse.model_validate(user)

    def create(self, user_data: UserCreate) -> UserResponse:
        user = self.repository.create(user_data)
        return UserResponse.model_validate(user)

    def upload(self, user_id: int, user_data: UserCreate) -> UserResponse:
        user = self.repository.upload(user_id, user_data)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with this id: {user_id} not found"
            )
        return UserResponse.model_validate(user)

    def delete_by_id(self, user_id: int) -> UserResponse:
        user = self.repository.delete_by_id(user_id)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with this id: {user_id} not found"
            )
        return UserResponse.model_validate(user)
