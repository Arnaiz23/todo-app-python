from datetime import datetime
from fastapi import HTTPException
from fastapi.responses import JSONResponse

import jwt

from ..models.models import CompletedTodoModel, CreateTodoModel

from ..libs import secret_key
from ..services.todosServices import (
    completedTodo,
    createTodo,
    deletedTodo,
    getTodos,
    updateTodo,
)


def getUserTodos(token):
    try:
        user_data = jwt.decode(token, secret_key, algorithms=["HS256"])
        todos = getTodos(user_data["id"])
        return todos
    except jwt.InvalidSignatureError as e:
        raise HTTPException(status_code=401)
    # TODO: Use this error in all the routes with token
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401)
    except Exception as e:
        statusCode = e.args[1]
        errorMessage = e.args[0]
        return JSONResponse(content={"error": errorMessage}, status_code=statusCode)


def createNewTodo(token, body: CreateTodoModel):
    try:
        user_data = jwt.decode(token, secret_key, algorithms=["HS256"])
        todo_data = {
            "title": body.title,
            "user_id": user_data["id"],
            "completed": False,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
        }

        todo_response = createTodo(todo_data)
        return todo_response
    except jwt.InvalidSignatureError as e:
        raise HTTPException(status_code=401)
    except Exception as e:
        statusCode = e.args[1]
        errorMessage = e.args[0]
        return JSONResponse(content={"error": errorMessage}, status_code=statusCode)


def updateTodoController(token, body: CreateTodoModel, todo_id):
    try:
        user_data = jwt.decode(token, secret_key, algorithms=["HS256"])
        todo_updated = updateTodo(todo_id, user_data["id"], body.title)
        return todo_updated
    except jwt.InvalidSignatureError:
        raise HTTPException(status_code=401)
    except Exception as e:
        statusCode = e.args[1]
        errorMessage = e.args[0]
        return JSONResponse(content={"error": errorMessage}, status_code=statusCode)


def updateTodoCompleted(token, body: CompletedTodoModel, id):
    todo_completed = body.completed

    try:
        user_login = jwt.decode(token, secret_key, algorithms=["HS256"])
        todo_updated = completedTodo(id, user_login["id"], todo_completed)

        return todo_updated
    except jwt.InvalidSignatureError:
        raise HTTPException(status_code=401)
    except Exception as e:
        statusCode = e.args[1]
        errorMessage = e.args[0]
        return JSONResponse(content={"error": errorMessage}, status_code=statusCode)


def deleteTodoController():
    todo_id = int(input("Enter the id of the todo: "))
    token = input("Token: ")

    try:
        user_login = jwt.decode(token, secret_key, algorithms=["HS256"])
        todo_deleted = deletedTodo(todo_id, user_login["id"])
        print(todo_deleted)
    except jwt.InvalidSignatureError:
        print(401)
    except Exception as e:
        # statusCode = e.args[1]
        errorMessage = e.args[0]
        print({"error": errorMessage})
