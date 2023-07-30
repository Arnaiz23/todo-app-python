from datetime import datetime

import jwt

from ..libs import secret_key
from ..services.todosServices import (
    completedTodo,
    createTodo,
    deletedTodo,
    getTodos,
    updateTodo,
)


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
    token = input("Token: ")

    try:
        user_data = jwt.decode(token, secret_key, algorithms=["HS256"])
        todo_updated = updateTodo(todo_id, user_data["id"], todo_title)
        print({"data": todo_updated})
    except jwt.InvalidSignatureError:
        print(401)
    except Exception as e:
        # statusCode = e.args[1]
        errorMessage = e.args[0]
        print({"error": errorMessage})


def updateTodoCompleted():
    todo_id = int(input("Enter the id of the todo: "))
    todo_completed = input("Enter the completed of the todo: ")
    token = input("Token: ")

    try:
        todo_completed = todo_completed.capitalize()

        if todo_completed == "True":
            todo_completed = True
        elif todo_completed == "False":
            todo_completed = False
        else:
            raise Exception("completed is missing", 400)

        user_login = jwt.decode(token, secret_key, algorithms=["HS256"])
        todo_updated = completedTodo(todo_id, user_login["id"], todo_completed)
        print({"data": todo_updated})
    except jwt.InvalidSignatureError:
        print(401)
    except Exception as e:
        # statusCode = e.args[1]
        errorMessage = e.args[0]
        print({"error": errorMessage})


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
