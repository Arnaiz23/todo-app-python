from .userServices import loginService
from .todosServices import getTodos

def getUserTodos():
    user_data = { "email": "adrian@gmail.com", "password": "adrian" }

    try:
        user_login = loginService(user_data)
        todos = getTodos(user_login['data'].get('id'))
        print({ "data": todos })
    except Exception as e:
        # statusCode = e.args[1]
        errorMessage = e.args[0]
        print({ "error": errorMessage })

