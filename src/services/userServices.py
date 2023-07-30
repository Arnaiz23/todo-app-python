from datetime import datetime
import json

import jwt
import bcrypt

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
    }

    token = jwt.encode(payload, secret_key)

    return {"data": token}


def registerService(user_data):
    with open("database/users.json", "r") as usersDatabase:
        data = json.load(usersDatabase)

        user_exits = next(
            filter(lambda x: x["email"] == user_data["email"], data), None
        )

        if user_exits:
            raise Exception("This email is already registered!!!", 409)

    # TODO: delete because the database will create for you
    user_data["created_at"] = datetime.now().isoformat()
    user_data["updated_at"] = datetime.now().isoformat()

    data.append(user_data)

    with open("database/users.json", "w") as usersDatabase:
        json.dump(data, usersDatabase, indent=2)

    user_data.pop("password")
    return {"data": user_data}


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
