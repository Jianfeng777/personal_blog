# seed_admin.py
from database import SessionLocal
from models import User

db = SessionLocal()

# 创建管理员账号
admin = User(username="admin", email="admin@example.com")
admin.set_password("123456")  # 设置初始密码

# 保存到数据库
db.add(admin)
db.commit()
db.close()

print("管理员账号已创建：用户名 admin / 密码 123456")
