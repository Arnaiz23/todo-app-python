import os
import json

from src.controllers.todosControllers import updateTodoController

def main():
    # Check if the usersDatabase exists or not, and create if not
    file_exists_user = os.path.isfile("database/users.json")
    if file_exists_user is False:
        json_data = json.dumps([])

        with open("database/users.json", "w") as usersDatabase:
            usersDatabase.write(json_data)

    file_exists_todos = os.path.isfile("database/todos.json")
    if file_exists_todos is False:
        json_data = json.dumps([])

        with open("database/todos.json", "w") as todosDatabase:
            todosDatabase.write(json_data)

    updateTodoController()

if __name__ == "__main__":
    main()
