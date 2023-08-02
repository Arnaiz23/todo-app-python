from fastapi import HTTPException
from fastapi.responses import JSONResponse

from ..libs import validate_email
from ..models.models import LoginForm, RegisterForm
from ..services.userServices import getUserInfo, loginService, registerService


def loginController(login: LoginForm):
    try:
        email = login.email
        password = login.password

        if validate_email(email) is False:
            raise Exception(f"The email {email} is not valid", 422)

        if password.__len__() < 6:
            raise ("Password must be at least 6 characters", 422)

        user_data = {"email": email, "password": password}

        result = loginService(user_data)
        return result
    except Exception as e:
        statusCode = e.args[1]
        errorMessage = e.args[0]
        return JSONResponse(content={"error": errorMessage}, status_code=statusCode)


def register(registerBody: RegisterForm):
    email, password, name, remember = registerBody.dict().values()

    try:
        if validate_email(email) is False:
            raise Exception(f"The email {email} is not valid", 422)

        if password.__len__() < 6:
            raise Exception("Password must be at least 6 characters", 422)

        user_data = {"email": email, "password": password, "name": name}

        result = registerService(user_data, remember)
        return result
    except Exception as e:
        statusCode = e.args[1]
        errorMessage = e.args[0]
        return JSONResponse(content={"error": errorMessage}, status_code=statusCode)


def user_info(token):
    try:
        result = getUserInfo(token)
        return result
    except Exception as e:
        statusCode = e.args[1]
        # errorMessage = e.args[0]
        raise HTTPException(status_code=statusCode)
