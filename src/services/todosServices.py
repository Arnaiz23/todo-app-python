import json

def getTodos(user_id):
    with open("database/todos.json", "r") as todosDB:
        data_json = json.load(todosDB)

    filter_todos = [todo for todo in data_json if todo.get('user_id') == user_id]

    return filter_todos

def createTodo(todo_data):
    with open("database/todos.json", "r") as todosDB:
        todos_db = json.load(todosDB)

    todos_db.append(todo_data)

    with open("database/todos.json", "w") as todosDB:
        json.dump(todos_db, todosDB, indent=2)

    return { "data": todo_data }
