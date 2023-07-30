import json

from sqlalchemy import and_

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


def mapOneTodo(todo):
    return {
        "id": todo.id,
        "title": todo.title,
        "completed": todo.completed,
        "created_at": todo.created_at,
        "updated_at": todo.updated_at,
        "user_id": todo.user_id,
    }


def getTodos(user_id):
    user_todos = session.query(Todos_model).filter(Todos_model.user_id == user_id).all()

    user_todos = mapTodos(user_todos)

    return user_todos


def createTodo(todo_data):
    try:
        new_todo = Todos_model(
            title=todo_data["title"],
            user_id=todo_data["user_id"],
            completed=False,
            created_at=todo_data["created_at"],
            updated_at=todo_data["updated_at"],
        )

        session.add(new_todo)
        session.commit()

        new_todo = mapOneTodo(new_todo)

        return new_todo
    except Exception as e:
        raise e


def updateTodo(todo_id, user_id, todo_title):
    try:
        user_todo = (
            session.query(Todos_model)
            .filter(and_(Todos_model.user_id == user_id, Todos_model.id == todo_id))
            .first()
        )

        user_todo.title = todo_title

        session.commit()

        user_todo = mapOneTodo(user_todo)

        return user_todo
    except Exception as e:
        raise Exception("This todo doesn't exists")


def completedTodo(todo_id, user_id, todo_completed):
    try:
        user_todo = (
            session.query(Todos_model)
            .filter(and_(Todos_model.user_id == user_id, Todos_model.id == todo_id))
            .first()
        )

        if user_todo is None:
            raise Exception("This todo doesn't exists")


        user_todo.completed = todo_completed

        session.commit()

        user_todo = mapOneTodo(user_todo)

        return user_todo
    except Exception as e:
        raise e


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
