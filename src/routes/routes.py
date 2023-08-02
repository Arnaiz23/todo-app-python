from fastapi import APIRouter, Request
from src.libs import getToken

from src.controllers.userControllers import loginController, register, user_info
from src.models.models import CreateTodoModel, LoginForm, RegisterForm
from src.controllers.todosControllers import createNewTodo, getUserTodos, updateTodoController

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
def get_user_todos_route(request: Request):
    token = getToken(request)

    return getUserTodos(token)

@route.post("/todos")
def create_todo_route(request: Request, body: CreateTodoModel):
    token = getToken(request)

    return createNewTodo(token, body)

@route.put("/todos/{id}")
def update_todo(request: Request, body: CreateTodoModel, id):
    token = getToken(request)

    return updateTodoController(token, body, id)

@route.delete("/todos/{id}")
def delete_todo(id: int):
    return {"route": f"Delete todo {id}"}
