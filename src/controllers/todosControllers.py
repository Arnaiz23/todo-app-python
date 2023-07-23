from datetime import datetime

from ..services.userServices import loginService
from ..services.todosServices import createTodo, getTodos


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
    # user_data = {"email": "adrian@gmail.com", "password": "adrian"}
    user_data = {"email": "test@gmail.com", "password": "test"}

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
