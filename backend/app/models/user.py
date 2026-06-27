from sqlalchemy import Column, Integer, String
from backend.app.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def __repr__(self):
        return f"<User: {self.username}; Mail: {self.email}>"