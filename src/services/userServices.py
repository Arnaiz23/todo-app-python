import datetime
import json

import bcrypt
import jwt
from sqlalchemy.exc import IntegrityError

from db import Base, session

User_model = Base.classes.users
secret_key = "secret_key"


def loginService(user_data):
    user_exists = (
        session.query(User_model)
        .filter(
            User_model.email == user_data["email"],
        )
        .first()
    )

    # If not exists, return
    if user_exists is None:
        raise Exception("The email or the password doesn't match", 404)

    if not bcrypt.checkpw(
        user_data["password"].encode("utf-8"),
        user_exists.password_hashed.encode("utf-8"),
    ):
        raise Exception("The email or the password doesn't match", 404)

    payload = {
        "id": user_exists.id,
        "name": user_exists.name,
        "email": user_exists.email,
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
    }

    token = jwt.encode(payload, secret_key)

    return {"data": token}


def registerService(user_data):
    password_hashed = bcrypt.hashpw(
        user_data["password"].encode("utf-8"), bcrypt.gensalt(10)
    )

    try:
        new_user = User_model(
            name=user_data["name"],
            email=user_data["email"],
            password_hashed=password_hashed,
        )

        session.add(new_user)

        session.commit()

        payload = {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email,
            "iat": datetime.datetime.utcnow(),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        }

        token = jwt.encode(payload, secret_key)

        return {"data": token}
    except IntegrityError as e:
        raise Exception("This email is already registered!!!", 409)


def getUserInfo(user_data):
    with open("database/users.json", "r") as usersDatabase:
        # data = list []
        data = json.load(usersDatabase)

        # Use the filter function for search if any user match with the user input
        user_exits = next(
            filter(lambda x: x["email"] == user_data["email"], data), None
        )

        # If not exists, return
        if user_exits is None:
            raise Exception("The email is incorrect", 404)

        # Compare the passwords
        if user_exits["password"] != user_data["password"]:
            raise Exception("The password not match")

    user_data.pop("password")
    return {"data": user_exits}
