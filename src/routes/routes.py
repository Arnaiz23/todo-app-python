from fastapi import APIRouter

from src.controllers.userControllers import loginController, register
from src.models.models import LoginForm, RegisterForm

route = APIRouter()


# User routes
@route.post("/login")
def login_route(login: LoginForm):
    return loginController(login)

@route.post("/register")
def login_route(registerBody: RegisterForm):
    return register(registerBody)


# Todos routes
@route.delete("/todos/{id}")
def deleteTodo(id: int):
    return {"route": f"Delete todo {id}"}
