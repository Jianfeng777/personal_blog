from fastapi import APIRouter

router = APIRouter(prefix="/api/users", tags=["Users"])

@router.get("/")
def list_users():
    return [{"id": 1, "username": "admin"}]
