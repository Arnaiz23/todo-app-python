from fastapi import APIRouter, Request

from src.controllers.todosControllers import (
    createNewTodo,
    deleteTodoController,
    getUserTodos,
    updateTodoCompleted,
    updateTodoController,
)
from src.controllers.userControllers import loginController, register, user_info
from src.libs import getToken
from src.models.models import (
    CompletedTodoModel,
    LoginForm,
    RegisterForm,
    TitleTodoModel,
)

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
def create_todo_route(request: Request, body: TitleTodoModel):
    token = getToken(request)

    return createNewTodo(token, body)


@route.put("/todos/{id}")
def update_todo(request: Request, body: TitleTodoModel, id):
    token = getToken(request)

    return updateTodoController(token, body, id)


@route.patch("/todos/{id}")
def update_completed_todo(request: Request, body: CompletedTodoModel, id):
    token = getToken(request)

    return updateTodoCompleted(token, body, id)


@route.delete("/todos/{id}", status_code=204)
def delete_todo(request: Request, id: int):
    token = getToken(request)

    return deleteTodoController(token, id)
