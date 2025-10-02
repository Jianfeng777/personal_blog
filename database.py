import os
from dotenv import load_dotenv

# 从 .env 文件中加载环境变量
load_dotenv()

# 从环境变量中获取数据库连接字符串
DATABASE_URL = os.getenv("DATABASE_URL")

print("数据库地址是：", DATABASE_URL)

from sqlalchemy import create_engine

# 创建数据库引擎（用于连接数据库）
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # 自动检测连接是否断开，断开就重连
    echo=True,           # 打印所有执行的 SQL（调试用）
    future=True          # 使用 SQLAlchemy 的 2.0 风格语法
)
print("数据库引擎创建成功")

from sqlalchemy.orm import sessionmaker

# 会话工厂，用于之后创建数据库连接会话对象（Session）
SessionLocal = sessionmaker(
    bind=engine,         # 绑定刚才创建的数据库引擎
    autoflush=False,     # 关闭自动刷新（手动控制更稳定）
    autocommit=False,    # 所有事务默认不自动提交（必须手动 .commit()）
    future=True          # 启用 SQLAlchemy 2.0 风格
)

from sqlalchemy.orm import declarative_base

# 所有 ORM 模型的基类
Base = declarative_base()

# FastAPI 依赖注入：获取一个数据库会话，用完后自动关闭
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()