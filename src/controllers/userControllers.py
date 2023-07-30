from ..libs import validate_email
from ..services.userServices import getUserInfo, loginService, registerService


def login():
    email = input("Enter the email: ")
    password = input("Enter the password: ")
    # print(f"Email: {email}, Password: {password}")

    if validate_email(email) is False:
        print(f"The email {email} is not valid")
        return

    if password.__len__() < 6:
        print("Password must be at least 6 characters")
        return

    user_data = {"email": email, "password": password}

    try:
        result = loginService(user_data)
        print(result)
    except Exception as e:
        # print(f"Error: {e}")
        # statusCode = e.args[1]
        errorMessage = e.args[0]
        print({"error": errorMessage})


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
