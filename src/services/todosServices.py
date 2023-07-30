import json

from db import Base, session

Todos_model = Base.classes.todos


def mapTodos(todos):
    todos_map = []
    for todo in todos:
        todos_map.append(
            {
                "id": todo.id,
                "title": todo.title,
                "completed": todo.completed,
                "created_at": todo.created_at,
                "updated_at": todo.updated_at,
            }
        )
    return todos_map


def getTodos(user_id):
    user_todos = session.query(Todos_model).filter(Todos_model.user_id == user_id).all()

    user_todos = mapTodos(user_todos)

    return user_todos


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

    indices = [index for index, todo in enumerate(data_json) if todo["id"] == todo_id]

    if not indices:
        raise Exception("This todo doesn't exists", 400)

    for index in indices:
        if data_json[index]["user_id"] != user_login["id"]:
            raise Exception("This user is not the owner of the todo")

        data_json[index]["title"] = todo_title
        todo_updated = data_json[index]

    with open("database/todos.json", "w") as todosDB:
        json.dump(data_json, todosDB, indent=2)

    return {"data": todo_updated}


def completedTodo(todo_id, user_login, todo_completed):
    with open("database/todos.json", "r") as todosDB:
        data_json = json.load(todosDB)

    indices = [index for index, todo in enumerate(data_json) if todo["id"] == todo_id]

    if not indices:
        raise Exception("This todo doesn't exists", 400)

    for index in indices:
        if data_json[index]["user_id"] != user_login["id"]:
            raise Exception("This user is not the owner of the todo")

        if data_json[index]["completed"] == todo_completed:
            raise Exception("This todo already have this value in the completed field")

        data_json[index]["completed"] = todo_completed
        todo_updated = data_json[index]

    with open("database/todos.json", "w") as todosDB:
        json.dump(data_json, todosDB, indent=2)

    return {"data": todo_updated}


def deletedTodo(todo_id, user_login):
    with open("database/todos.json", "r") as todosDB:
        data_json = json.load(todosDB)

    indices = [index for index, todo in enumerate(data_json) if todo["id"] == todo_id]

    if not indices:
        raise Exception("This todo doesn't exists", 400)

    if data_json[indices[0]]["user_id"] != user_login["id"]:
        raise Exception("This user is not the owner of the todo")

    del data_json[indices[0]]

    with open("database/todos.json", "w") as todosDB:
        json.dump(data_json, todosDB, indent=2)

    return 204
