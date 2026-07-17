from fastapi import APIRouter, Depends

from dependencies import get_current_user

from database import SessionLocal

from models import User

from schemas import UserResponse


router = APIRouter()



# 获取自己的信息
@router.get("/user/info")
def get_user_info(
    current_user: User = Depends(get_current_user)
):

    return {
        "id": current_user.id,
        "username": current_user.username
    }



# 获取所有用户
@router.get(
    "/users",
    response_model=list[UserResponse]
)
def get_users():

    db = SessionLocal()

    try:

        users = db.query(User).all()

        return users

    finally:

        db.close()