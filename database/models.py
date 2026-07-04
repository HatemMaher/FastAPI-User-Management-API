from sqlalchemy import Column, Integer, String, Boolean

from database.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    email = Column(String)

    is_active = Column(Boolean, default=True)