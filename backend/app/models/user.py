from sqlalchemy import Column, Integer, String
from ..database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f"<User: {self.username}; Mail: {self.email}>"
