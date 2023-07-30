from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.controllers.userControllers import loginController
from src.models.models import CustomHttpException, LoginForm

route = APIRouter()


# User routes
@route.post("/login")
def login_route(login: LoginForm):
    try:
        token = loginController(login)

        return token
    except Exception as e:
        errorMessage = e.args[0]
        statusCode = e.args[1]
        return JSONResponse(content={"error": errorMessage}, status_code=statusCode)


# Todos routes
@route.delete("/todos/{id}")
def deleteTodo(id: int):
    return {"route": f"Delete todo {id}"}
