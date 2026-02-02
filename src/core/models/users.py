from core.base import Base

from sqlalchemy import Column, String


class Users(Base):
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    