from fastapi import APIRouter

from src.controllers.userControllers import loginController
from src.models.models import LoginForm

route = APIRouter()


# User routes
@route.post("/login")
def login_route(login: LoginForm):
    return loginController(login)


# Todos routes
@route.delete("/todos/{id}")
def deleteTodo(id: int):
    return {"route": f"Delete todo {id}"}
