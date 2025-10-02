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
