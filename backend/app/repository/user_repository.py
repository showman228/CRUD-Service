from sqlalchemy.orm import Session, joinedload
from typing import List
from backend.app.models.user import User
from backend.app.schemas.user import UserCreate


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()

    def get_all(self) -> List[User]:
        return self.db.query(User).all()

    def get_by_email(self, user_email: str) -> User:
        return self.db.query(User).filter(User.email == user_email).first()

    def get_by_username(self, username: str) -> User:
        return self.db.query(User).filter(User.username == username).first()

    def create(self, user_data: UserCreate) -> User:
        db_user = User(**user_data.model_dump())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def upload(self, user_id: int, user_data: UserCreate) -> User:
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if db_user is None:
            return None
        for key, value in user_data.model_dump().items():
            setattr(db_user, key, value)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete_by_id(self, id: int) -> User:
        db_user = self.db.query(User).filter(User.id == id).first()
        if db_user is None:
            return None
        self.db.delete(db_user)
        self.db.commit()
        return db_user
