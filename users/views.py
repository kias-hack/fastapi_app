from fastapi import APIRouter

from users.schemas import CreateUserRequest

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/users/")
def create_user(request: CreateUserRequest):
    return {
        "status": "success",
        "user": {
            "login": request.login,
            "email": request.email,
        }
    }