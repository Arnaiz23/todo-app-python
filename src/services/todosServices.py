from sqlalchemy import and_

from db import get_engine

from ..libs import mapOneTodo, mapTodos

session, Base = get_engine()
Todos_model = Base.classes.todos


def getTodos(user_id):
    user_todos = session.query(Todos_model).filter(Todos_model.user_id == user_id).all()

    user_todos = mapTodos(user_todos)

    return {"data": user_todos}


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

        return {"data": new_todo}
    except Exception as e:
        raise e


def updateTodo(todo_id, user_id, todo_title):
    try:
        user_todo = (
            session.query(Todos_model)
            .filter(and_(Todos_model.user_id == user_id, Todos_model.id == todo_id))
            .first()
        )

        if user_todo is None:
            raise Exception("This todo doesn't exists", 404)

        user_todo.title = todo_title

        session.commit()

        user_todo = mapOneTodo(user_todo)

        return {"data": user_todo}
    except Exception as e:
        # raise Exception("This todo doesn't exists", 404)
        raise e


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

        return {"data": user_todo}
    except Exception as e:
        raise e


def deletedTodo(todo_id, user_id):
    try:
        todo = (
            session.query(Todos_model)
            .filter(and_(Todos_model.id == todo_id, Todos_model.user_id == user_id))
            .first()
        )

        if todo is None:
            raise Exception("This todo doesn't exists", 404)

        session.delete(todo)
        session.commit()

        return 204
    except Exception as e:
        raise e
