from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt, JWTError

from database import SessionLocal
from models import User

from security import SECRET_KEY, ALGORITHM


oauth2_scheme = HTTPBearer()


def get_current_user(
    credentials=Depends(oauth2_scheme)
):

    token = credentials.credentials

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(
                status_code=401,
                detail="Token无效"
            )


        db = SessionLocal()

        try:

            user = (
                db.query(User)
                .filter(User.id == int(user_id))
                .first()
            )


            if user is None:
                raise HTTPException(
                    status_code=404,
                    detail="用户不存在"
                )


            return user


        finally:
            db.close()


    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Token无效"
        )