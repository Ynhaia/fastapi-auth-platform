#注册登录
from fastapi import APIRouter

from database import SessionLocal

from schemas import UserCreate, UserLogin

from models import User

from security import (
    hash_password,
    verify_password,
    create_access_token
)

router=APIRouter()

@router.post("/register")
def register(user: UserCreate):

    db = SessionLocal()

    try:

        exist_user = (
            db.query(User)
            .filter(User.username == user.username)
            .first()
        )


        if exist_user:
            return {
                "msg":"用户已存在"
            }


        hashed_password = hash_password(
            user.password
        )


        db_user = User(
            username=user.username,
            password=hashed_password
        )


        db.add(db_user)

        db.commit()

        db.refresh(db_user)


        return {
            "msg":"注册成功",
            "id":db_user.id
        }


    finally:
        db.close()


@router.post("/login")
def login(user: UserLogin):

    db = SessionLocal()

    try:

        db_user = (
            db.query(User)
            .filter(User.username == user.username)
            .first()
        )


        if not db_user:

            return {
                "msg":"用户名或密码错误"
            }


        if not verify_password(
            user.password,
            db_user.password
        ):

            return {
                "msg":"用户名或密码错误"
            }


        token = create_access_token(
    {
        "sub":str(db_user.id)
    }
)


        return {
            "access_token":token,
            "token_type":"bearer"
        }


    finally:
        db.close()
        