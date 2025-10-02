from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from database import get_db
from models import User
from auth_utils import create_access_token, verify_token
from auth_settings import ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta
from fastapi.security import OAuth2PasswordBearer

# 路由对象
router = APIRouter(prefix="/api/auth", tags=["Auth"])

# 登录请求体
class LoginInput(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=3, max_length=100)

# 测试接口
@router.get("/ping")
def ping():
    return {"message": "auth 路由工作正常"}

# 登录接口
@router.post("/login")
def login(data: LoginInput, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    
    if not user.check_password(data.password):
        raise HTTPException(status_code=401, detail="密码错误")

    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {
        "message": "登录成功",
        "access_token": access_token,
        "token_type": "bearer"
    }

# 用 token 访问的受保护接口
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@router.get("/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    return {"message": "你是管理员用户", "username": payload["sub"]}
