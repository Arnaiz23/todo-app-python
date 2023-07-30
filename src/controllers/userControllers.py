from fastapi import HTTPException

from ..libs import validate_email
from ..models.models import LoginForm
from ..services.userServices import getUserInfo, loginService, registerService


def loginController(login: LoginForm):
    email = login.email
    password = login.password

    if validate_email(email) is False:
        raise Exception(f"The email {email} is not valid", 422)

    if password.__len__() < 6:
        raise("Password must be at least 6 characters", 422)

    user_data = {"email": email, "password": password}

    try:
        result = loginService(user_data)
        return result
    except Exception as e:
        statusCode = e.args[1]
        errorMessage = e.args[0]
        raise Exception(errorMessage, statusCode)


def register():
    email = input("Enter the email: ")
    password = input("Enter the password: ")
    name = input("Enter the name: ")
    remember = int(input("1 or 2"))

    if validate_email(email) is False:
        print(f"The email {email} is not valid")
        return

    if password.__len__() < 6:
        print("Password must be at least 6 characters")
        return

    user_data = {"email": email, "password": password, "name": name}

    try:
        result = registerService(user_data, remember)
        print(result)
    except Exception as e:
        # statusCode = e.args[1]
        errorMessage = e.args[0]
        print({"error": errorMessage})


def user_info():
    code = input("Token: ")

    try:
        result = getUserInfo(code)
        print(result)
    except Exception as e:
        # print(f"Error: {e}")
        # statusCode = e.args[1]
        errorMessage = e.args[0]
        print({"error": errorMessage})
