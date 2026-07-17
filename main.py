from fastapi import FastAPI

from routers import auth
from routers import user

from models import Base
from database import engine


app = FastAPI()


# 注册路由

app.include_router(
    auth.router
)


app.include_router(
    user.router
)



@app.get("/")
def hello():

    return {
        "msg":"数据库连接成功"
    }



Base.metadata.create_all(
    bind=engine
)