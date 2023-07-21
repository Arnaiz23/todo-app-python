import json

def getTodos(user_id):
    with open("database/todos.json", "r") as todosDB:
        data_json = json.load(todosDB)

    filter_todos = [todo for todo in data_json if todo.get('user_id') == user_id]

    return filter_todos
