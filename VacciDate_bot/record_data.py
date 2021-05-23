import json


def remove_record(user_data):
    print(user_data)
    username = user_data.message.from_user.username
    if username is None:
        first_name = user_data.message.from_user.first_name
        chat_id = user_data.message.from_user.id
        username = f"{first_name}_{chat_id}"
    with open("data/user_data.json", "r") as f:
        data = json.load(f)
        f.close()
    user_data = data["user_data"]
    user_data.pop(username, None)
    data.update({"user_data": user_data})
    with open("data/user_data.json", "w") as f:
        json.dump(data, f)
        f.close()


def store_data(district_id, user_data):
    print(user_data)
    first_name = user_data.message.from_user.first_name
    last_name = user_data.message.from_user.last_name
    username = user_data.message.from_user.username
    print(f"{username=}")
    print(f"{type(username)}")
    chat_id = user_data.message.from_user.id
    if username is None:
        username = f"{first_name}_{chat_id}"
    print(f"{username=}")
    with open("data/user_data.json", "r") as f:
        data = json.load(f)
        f.close()
    user_data = data["user_data"]
    existing_user = user_data.get(username, None)
    if existing_user is None:
        user_data.update(
            {
                username: {
                    "first_name": first_name,
                    "last_name": last_name,
                    "chat_id": chat_id,
                    "districts": [district_id],
                    "age_groups": [],
                }
            }
        )
    else:
        dist_list = existing_user.get("districts")
        if district_id in dist_list:
            return True
        dist_list.append(district_id)
        existing_user["districts"] = dist_list
        user_data.update({username: existing_user})
    data.update({"user_data": user_data})
    with open("data/user_data.json", "w") as f:
        json.dump(data, f)
        f.close()


def update_age_group(age_group, user_data):
    print(user_data)
    first_name = user_data.message.from_user.first_name
    chat_id = user_data.message.from_user.id
    age_group = int(age_group.split("+")[0])
    username = user_data.message.from_user.username
    print(f"{type(username)}")
    print(f"{username}")
    if username is None:
        username = f"{first_name}_{chat_id}"
    print(f"{username=}")
    with open("data/user_data.json", "r") as f:
        data = json.load(f)
        f.close()
    user_data = data["user_data"]
    existing_user = user_data.get(username, None)
    if existing_user is None:
        return "User does not exist. Please register before updating age group"
    else:
        age_group_list = existing_user.get("age_groups")
        if age_group in age_group_list:
            return True
        age_group_list.append(age_group)
        existing_user["age_groups"] = age_group_list
        user_data.update({username: existing_user})
    data.update({"user_data": user_data})
    with open("data/user_data.json", "w") as f:
        json.dump(data, f)
        f.close()
