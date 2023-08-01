from re import split
from fastapi import APIRouter, Request

from src.controllers.userControllers import loginController, register, user_info
from src.models.models import LoginForm, RegisterForm

route = APIRouter()


# User routes
@route.post("/login")
def login_route(login: LoginForm):
    return loginController(login)

@route.post("/register")
def login_route(registerBody: RegisterForm):
    return register(registerBody)

@route.get("/users")
def login_route(request: Request):
    token_header = request.headers['authorization']
    token_split = split(" ", token_header)
    token = token_split[1]

    return user_info(token)


# Todos routes
@route.delete("/todos/{id}")
def deleteTodo(id: int):
    return {"route": f"Delete todo {id}"}
