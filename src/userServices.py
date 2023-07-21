import json


def loginService(user_data):
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

        return {"data": user_exits}


def registerService(user_data):
    with open("database/users.json", "r") as usersDatabase:
        data = json.load(usersDatabase)

        user_exits = next(filter(lambda x: x["email"] == user_data["email"], data), None)

        if user_exits:
            raise Exception("This email is already registered!!!", 409)



    data.append(user_data)

    with open("database/users.json", "w") as usersDatabase:
        json.dump(data, usersDatabase, indent=2)

    return { "data": user_data }

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

        return {"data": user_exits}
