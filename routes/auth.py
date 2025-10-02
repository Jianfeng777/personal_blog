from fastapi import APIRouter

auth_router = APIRouter(prefix="/api/auth", tags=["Auth"])

@auth_router.get("/ping")
def ping():
    return {"message": "auth 路由工作正常"}
