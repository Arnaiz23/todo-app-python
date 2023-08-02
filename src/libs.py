from re import match, split

from fastapi import Request


def validate_email(email):
    if match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False


secret_key = "secret_key"


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


def getToken(request: Request):
    token_header = request.headers["authorization"]
    token_split = split(" ", token_header)
    return token_split[1]
