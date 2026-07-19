from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class User(Base):

    __tablename__ = "users"


    id = Column(
        Integer,
        primary_key=True
    )


    username = Column(
        String(50),
        unique=True,
        nullable=False
    )


    password = Column(
        String(100),
        nullable=False
    )


    role = Column(
        String(20),
        default="user"
    )


    status = Column(
        String(20),
        default="active"
    )