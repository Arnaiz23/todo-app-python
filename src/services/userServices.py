import datetime

import bcrypt
import jwt
from sqlalchemy.exc import IntegrityError

from db import Base, session

from ..libs import secret_key

User_model = Base.classes.users


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


def registerService(user_data, remember):
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
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=remember),
        }

        token = jwt.encode(payload, secret_key)

        return {"data": token}
    except IntegrityError as e:
        raise Exception("This email is already registered!!!", 409)


def getUserInfo(code):
    try:
        user_data = jwt.decode(code, secret_key, algorithms=["HS256"])

        user_exists = (
            session.query(User_model)
            .filter(user_data["email"] == User_model.email)
            .first()
        )

        user_response = {
            "id": user_exists.id,
            "name": user_exists.name,
            "email": user_exists.email,
            "created_at": user_exists.created_at,
            "updated_at": user_exists.updated_at,
        }

        return {"data": user_response}
    except Exception as e:
        raise Exception("401", 401)
