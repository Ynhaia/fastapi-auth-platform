# FastAPI User Authentication System

基于 FastAPI + MySQL + SQLAlchemy + JWT + RBAC 实现的用户认证与权限管理系统。

本项目模拟企业后台用户管理系统，实现用户注册、登录认证、JWT身份校验、角色权限控制以及管理员账号管理功能。

同时使用 pytest + requests 构建接口自动化测试体系，并通过 Allure生成测试报告。

本项目主要实现用户注册、登录认证、密码加密存储以及基于 JWT Token 的接口访问控制。

项目按照实际后端开发模式进行模块化设计，将路由、数据库、认证、安全逻辑进行分层管理。


---

## 项目背景

传统 Web 应用中，用户认证通常包含：

- 用户注册
- 密码安全存储
- 用户登录验证
- 身份认证
- 用户信息获取

本项目模拟企业后端用户系统，实现完整认证流程。


---

# 技术栈

## 后端框架

- FastAPI

## 数据库

- MySQL

## ORM

- SQLAlchemy

## 数据校验

- Pydantic

## 身份认证

- JWT(JSON Web Token)


## 权限控制

- RBAC(Role-Based Access Control)
- 用户角色管理
- 管理员权限控制


## 密码安全

- bcrypt

## 测试

- pytest
- requests
- Allure


---

# 已实现功能


## 用户注册

- 用户名唯一校验
- 密码 bcrypt 加密
- 用户信息保存 MySQL


接口：

```
POST /register
```


请求：

```json
{
    "username":"admin",
    "password":"123456"
}
```


返回：

```json
{
    "msg":"注册成功",
    "id":1
}
```



---

## 用户登录

功能：

- 用户查询
- bcrypt密码验证
- JWT Token生成


接口：

```
POST /login
```


返回：

```json
{
    "access_token":"xxxxx",
    "token_type":"bearer"
}
```



---

## JWT身份认证


登录成功后获取 Token。


访问受保护接口时：

```
Authorization: Bearer Token
```


系统流程：

```
客户端请求
      |
      ↓
携带JWT Token
      |
      ↓
解析Token
      |
      ↓
获取用户ID
      |
      ↓
查询数据库
      |
      ↓
返回用户信息
```



---

## 获取用户信息


接口：

```
GET /user/info
```


需要携带JWT Token。


返回：

```json
{
    "id":1,
    "username":"admin"
}
```



---

## 用户列表查询


接口：

```
GET /users
```


返回数据库中的用户信息。


接口使用 Pydantic Response Model 对返回数据进行过滤，避免密码字段泄露。


---

---

# 接口自动化测试


本项目使用 pytest + requests 对核心接口进行自动化测试。


测试覆盖：


## 用户认证

- 用户注册成功
- 用户登录成功


## 用户接口

- 携带JWT Token获取用户信息
- Token权限校验


## 管理员权限

- 管理员查询用户列表
- 管理员冻结普通用户
- 管理员恢复普通用户


运行测试：

```bash
pytest
生成Allure报告：

pytest --alluredir=allure-results

查看报告：

allure serve allure-results


## 角色权限管理


系统采用 RBAC 权限模型，根据用户角色控制接口访问权限。


目前支持角色：

- admin 管理员
- user 普通用户


权限流程：

---

## 用户状态管理


系统支持用户状态控制。


用户状态：

- active 正常用户
- frozen 冻结用户


冻结后：

- 用户无法登录系统
- 已有权限接口无法继续访问


管理员可以执行：

- 冻结普通用户
- 恢复用户状态


接口：


---

# 项目结构


```
fastapi_demo

├── main.py                 # 项目入口

├── database.py             # 数据库连接配置

├── models.py               # SQLAlchemy数据库模型

├── schemas.py              # Pydantic数据模型

├── security.py             # JWT与密码加密逻辑

├── dependencies.py         # Token认证依赖


├── routers

│   ├── auth.py             # 注册、登录接口

│   ├── user.py             # 用户信息接口

│   └── admin.py            # 管理员权限接口


├──tests

│   ├── test_auth.py        # 认证测试

│   ├── test_user.py        # 用户接口测试

│   └── test_admin.py       # 管理员权限测试


├── requirements.txt

└── README.md

```



---

# 核心设计


## 密码安全

用户注册时：

```
明文密码
      |
      ↓
bcrypt + salt
      |
      ↓
哈希密码
      |
      ↓
保存数据库
```


数据库不会保存用户明文密码。



---

## JWT认证设计


Token中保存：

```json
{
    "sub":"用户ID",
    "role":"admin",
    "exp":"过期时间"
}
```


请求接口：

```
JWT
 |
 ↓
解析用户ID和角色
 |
 ↓
查询用户信息
 |
 ↓
验证用户状态
 |
 ↓
判断接口权限
 |
 ↓
执行接口逻辑
```



---

# 环境要求


Python:

```
Python 3.10+
```


MySQL:

```
MySQL 8.0+
```



---

# 安装运行


## 1. 克隆项目


```bash
git clone 项目地址
```



## 2. 创建虚拟环境


```bash
python -m venv venv
```


激活：

Windows:

```bash
venv\Scripts\activate
```



---

## 3. 安装依赖


```bash
pip install -r requirements.txt
```



---

## 4. 配置数据库


修改：

```
database.py
```


配置 MySQL：

```python
DATABASE_URL = "mysql+pymysql://用户名:密码@localhost/数据库名"
```



---

## 5. 启动项目


```bash
uvicorn main:app --reload
```


访问：

```
http://127.0.0.1:8000/docs
```


使用 Swagger UI 测试接口。



---

# 后续规划


# 后续规划


## v2.1

- 优化测试数据管理
- 增加pytest fixture
- 增加异常场景测试


## v2.2

- Docker部署
- Redis缓存
- CI/CD自动化测试流程

---

# 项目收获

通过本项目学习并实践：

- FastAPI项目结构设计
- RESTful API开发
- MySQL数据库操作
- SQLAlchemy ORM使用
- JWT认证流程
- bcrypt密码安全
- 后端模块化开发
- RBAC权限模型设计
- 用户状态管理
- 管理员接口开发

