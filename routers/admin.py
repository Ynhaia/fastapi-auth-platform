from fastapi import APIRouter, Depends

from dependencies import require_admin

from database import SessionLocal

from models import User

from schemas import UserResponse

from fastapi import HTTPException

router = APIRouter()


@router.get(
    "/admin/users",
    response_model=list[UserResponse]
)
def get_all_users(
    admin: User = Depends(require_admin)
):

    db = SessionLocal()

    try:

        users = db.query(User).all()

        return users

    finally:

        db.close()



@router.put("/admin/users/{user_id}/disable")
def disable_user(
    user_id:int,
    admin:User=Depends(require_admin)
):

    db=SessionLocal()

    try:

        user = (
            db.query(User)
            .filter(User.id==user_id)
            .first()
        )


        if not user:

            raise HTTPException(
                status_code=404,
                detail="用户不存在"
            )


        user.status="disabled"

        db.commit()


        return {
            "msg":"账号已冻结"
        }


    finally:

        db.close()



@router.put("/admin/users/{user_id}/enable")
def enable_user(
    user_id:int,
    admin:User=Depends(require_admin)
):

    db=SessionLocal()

    try:

        user = (
            db.query(User)
            .filter(User.id==user_id)
            .first()
        )


        if not user:

            raise HTTPException(
                status_code=404,
                detail="用户不存在"
            )


        user.status="active"

        db.commit()


        return {
            "msg":"账号已恢复"
        }


    finally:

        db.close()