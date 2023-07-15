import os
import json

from src.userControllers import register

def main():
    # Check if the usersDatabase exists or not, and create if not
    file_exists = os.path.isfile("database/users.json")
    if file_exists is False:
        json_data = json.dumps([])

        with open("database/users.json", "w") as usersDatabase:
            usersDatabase.write(json_data)

    # Execute the register route
    register()


if __name__ == "__main__":
    main()
