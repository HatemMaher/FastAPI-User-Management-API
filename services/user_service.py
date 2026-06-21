users = [
    {
        "id": 1,
        "name": "Hatem"
    },
    {
        "id": 2,
        "name": "Ahmed"
    }
]

def get_all_users():
    return users


def get_user_by_id(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user

    return None


def create_user(name: str):
    new_user = {
        "id": len(users) + 1,
        "name": name
    }

    users.append(new_user)

    return new_user

def update_user(user_id: int, name: str):

    for user in users:

        if user["id"] == user_id:

            user["name"] = name

            return user

    return None

def delete_user(user_id: int):

    for index, user in enumerate(users):

        if user["id"] == user_id:

            deleted_user = users.pop(index)

            return deleted_user

    return None