import json

with open("data/users.json", "r") as file:
    data = json.load(file)


count = 0


def check_login(username, password):
    for i in range(len(data["users"])):
        if (
            data["users"][i]["username"] == username
            and data["users"][i]["password"] == password
        ):
            return True

    return False


def login(username, password):
    global count

    if count >= 3:
        return [False, "Anda di blokir dari program karena gagal login selama 3 kali"]

    if check_login(username, password):
        return [True, "Login berhasil"]

    count += 1

    if count == 3:
        return [False, "Anda di blokir dari program karena gagal login selama 3 kali"]

    return [False, f"Login gagal. Percobaan {count}/3"]