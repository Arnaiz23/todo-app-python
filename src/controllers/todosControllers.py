from datetime import datetime
import jwt

from ..services.userServices import loginService
from ..services.todosServices import (
    completedTodo,
    createTodo,
    deletedTodo,
    getTodos,
    updateTodo,
)
from ..libs import secret_key


def getUserTodos():
    token = input("Token: ")

    try:
        user_data = jwt.decode(token, secret_key, algorithms=["HS256"])
        todos = getTodos(user_data["id"])
        print({"data": todos})
    except jwt.InvalidSignatureError as e:
        print(401)
    except Exception as e:
        # statusCode = e.args[1]
        errorMessage = e.args[0]
        print({"error": errorMessage})


def createNewTodo():
    todo_title = input("Enter the title of the todo: ")
    token = input("Token: ")

    try:
        user_data = jwt.decode(token, secret_key, algorithms=["HS256"])
        todo_data = {
            "title": todo_title,
            "user_id": user_data["id"],
            "completed": False,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
        }

        todo_response = createTodo(todo_data)
        print({"data": todo_response})
    except jwt.InvalidSignatureError as e:
        print(401)
    except Exception as e:
        # statusCode = e.args[1]
        errorMessage = e.args[0]
        print({"error": errorMessage})


def updateTodoController():
    todo_id = int(input("Enter the id of the todo: "))
    todo_title = input("Enter the new title: ")
    user_data = {"email": "adrian@gmail.com", "password": "adrian"}

    try:
        user_login = loginService(user_data)
        todo_updated = updateTodo(todo_id, user_login["data"], todo_title)
        print(todo_updated)
    except Exception as e:
        # statusCode = e.args[1]
        errorMessage = e.args[0]
        print({"error": errorMessage})


def updateTodoCompleted():
    todo_id = int(input("Enter the id of the todo: "))
    todo_completed = input("Enter the completed of the todo: ")
    user_data = {"email": "adrian@gmail.com", "password": "adrian"}

    try:
        todo_completed = todo_completed.capitalize()

        if todo_completed == "True":
            todo_completed = True
        elif todo_completed == "False":
            todo_completed = False
        else:
            raise Exception("completed is missing", 400)

        user_login = loginService(user_data)
        todo_updated = completedTodo(todo_id, user_login["data"], todo_completed)
        print(todo_updated)
    except Exception as e:
        # statusCode = e.args[1]
        errorMessage = e.args[0]
        print({"error": errorMessage})


def deleteTodoController():
    todo_id = int(input("Enter the id of the todo: "))
    user_data = {"email": "adrian@gmail.com", "password": "adrian"}

    try:
        user_login = loginService(user_data)
        todo_deleted = deletedTodo(todo_id, user_login["data"])
        print(todo_deleted)
    except Exception as e:
        # statusCode = e.args[1]
        errorMessage = e.args[0]
        print({"error": errorMessage})
