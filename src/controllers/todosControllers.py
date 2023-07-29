from datetime import datetime
from os import EX_CONFIG

from ..services.userServices import loginService
from ..services.todosServices import completedTodo, createTodo, getTodos, updateTodo


def getUserTodos():
    user_data = {"email": "adrian@gmail.com", "password": "adrian"}

    try:
        user_login = loginService(user_data)
        todos = getTodos(user_login["data"].get("id"))
        print({"data": todos})
    except Exception as e:
        # statusCode = e.args[1]
        errorMessage = e.args[0]
        print({"error": errorMessage})


def createNewTodo():
    todo_title = input("Enter the title of the todo: ")
    user_data = {"email": "adrian@gmail.com", "password": "adrian"}

    try:
        user_login = loginService(user_data)
        todo_data = {
            "title": todo_title,
            "user_id": user_login["data"]["id"],
            "completed": False,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
        }

        todo_response = createTodo(todo_data)
        print(todo_response)
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
        todo_updated = completedTodo(todo_id, user_login['data'], todo_completed)
        print(todo_updated)
    except Exception as e:
        # statusCode = e.args[1]
        errorMessage = e.args[0]
        print({"error": errorMessage})
