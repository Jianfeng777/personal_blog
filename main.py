from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Blog API")

from database import engine, Base
from models import User

# 在服务启动时，自动根据模型创建表结构（开发时用）
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import get_db

# 测试数据库连通性
@app.get("/api/debug/db-ok")
def db_ok(db: Session = Depends(get_db)):
    version = db.execute(text("SELECT VERSION()")).scalar()
    user_count = db.execute(text("SELECT COUNT(*) FROM users")).scalar()
    return {
        "mysql_version": version,
        "users_count": user_count
    }


# 允许跨域（以后前端 Vue/React 要访问）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 开发环境先放开，生产再限制
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
async def health():
    return {"ok": True, "service": "blog-api"}

