from .userServices import loginService, registerService
from .libs import validate_email

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
        print({ "error": errorMessage })

def register():
    # email = input("Enter the email: ")
    # password = input("Enter the password: ")
    # name = input("Enter the name: ")
    #
    # if validate_email(email) is False:
    #     print(f"The email {email} is not valid")
    #     return
    #
    # if password.__len__() < 6:
    #     print("Password must be at least 6 characters")
    #     return
    #
    # user_data = { "email": email, "password": password, "name": name }
    user_data = { "email": "adrian1@gmail.com", "password": "adrian", "name": "adrian" }

    try:
        result = registerService(user_data)
        print(result)
    except Exception as e:
        # statusCode = e.args[1]
        errorMessage = e.args[0]
        print({ "error": errorMessage })
