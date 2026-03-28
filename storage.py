import json
import os

DEFAULT_DATA = {
    "income": [],
    "budget": [],
    "expense": [],
    "savings": [],
    "savings_goal": {},
    "lent": [],
    "borrowed": []
}

DATA_FOLDER = "user_data"

if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

CURRENT_USER = {}

def set_current_user(user_data):
    global CURRENT_USER
    CURRENT_USER = user_data.copy()

def get_user_path(email):
    safe_email = email.replace("@", "_at_").replace(".", "_dot_")
    return os.path.join(DATA_FOLDER, f"{safe_email}.json")

def read_data(email):
    PATH = get_user_path(email)

    if not os.path.exists(PATH):
        return DEFAULT_DATA.copy()  

    with open(PATH, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = DEFAULT_DATA.copy()

    for key, value in DEFAULT_DATA.items():
        if key not in data:
            data[key] = value
    return data

def save_data(data, email=None):
    if email is None:
        email = CURRENT_USER["email"]

    PATH = get_user_path(email)
    with open(PATH, "w") as f:
        json.dump(data, f, indent=4)