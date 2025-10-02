from sqlalchemy import Column, Integer, String, DateTime, func
from database import Base
from passlib.hash import pbkdf2_sha256

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    email = Column(String(100), nullable=True)
    created_at = Column(DateTime, server_default=func.now())

    # 设置密码（使用 pbkdf2_sha256）
    def set_password(self, password: str):
        self.password_hash = pbkdf2_sha256.hash(password)

    # 校验密码
    def check_password(self, password: str) -> bool:
        return pbkdf2_sha256.verify(password, self.password_hash)
