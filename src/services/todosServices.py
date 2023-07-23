import json


def getTodos(user_id):
    with open("database/todos.json", "r") as todosDB:
        data_json = json.load(todosDB)

    filter_todos = [todo for todo in data_json if todo.get("user_id") == user_id]

    return filter_todos


def createTodo(todo_data):
    with open("database/todos.json", "r") as todosDB:
        todos_db = json.load(todosDB)

    todos_db.append(todo_data)

    with open("database/todos.json", "w") as todosDB:
        json.dump(todos_db, todosDB, indent=2)

    return {"data": todo_data}


def updateTodo(todo_id, user_login, todo_title):
    with open("database/todos.json", "r") as todosDB:
        data_json = json.load(todosDB)

    todo_filter = next(filter(lambda v: v["id"] == todo_id, data_json), None)

    if todo_filter is None:
        raise Exception("This todo doesn't exists", 400)

    if todo_filter['user_id'] != user_login['id']:
        raise Exception("This user is not the owner of the todo")

    # Update the title

    return todo_filter
