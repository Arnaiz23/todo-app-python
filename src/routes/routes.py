from fastapi import APIRouter, Request
from src.libs import getToken

from src.controllers.userControllers import loginController, register, user_info
from src.models.models import LoginForm, RegisterForm
from src.controllers.todosControllers import getUserTodos

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
    token = getToken(request)

    return user_info(token)


# Todos routes
@route.get("/todos")
def getUserTodosRoute(request: Request):
    token = getToken(request)

    return getUserTodos(token)

@route.delete("/todos/{id}")
def deleteTodo(id: int):
    return {"route": f"Delete todo {id}"}
