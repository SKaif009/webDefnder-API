from fastapi import APIRouter
from models.userModel import UserModel, LoginModel
from controllers.userControl import UserController

router = APIRouter()

@router.post("/register")
async def register_user(register: UserModel):
    result = await UserController.register_user(register)
    return result  # Make sure we're returning this correctly

@router.post("/login")
async def login_user(login: LoginModel):
    print("Login route hit")
    result = await UserController.login_user(login.email, login.password)
    return result