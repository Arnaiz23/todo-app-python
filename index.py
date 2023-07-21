import os
import json

from src.userControllers import register, user_info

def main():
    # Check if the usersDatabase exists or not, and create if not
    file_exists = os.path.isfile("database/users.json")
    if file_exists is False:
        json_data = json.dumps([])

        with open("database/users.json", "w") as usersDatabase:
            usersDatabase.write(json_data)

    user_info()

if __name__ == "__main__":
    main()
