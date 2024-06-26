from db import DBInterface
from app import login_manager
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id, username, password, name, lastname):
        self.id = id
        self.username = username
        self.password = password
        self.name = name
        self.lastname = lastname


@login_manager.user_loader
def load_user(id):
    try:
        db = DBInterface()

        login, password, role = db.getUserLogPassByID(id)

        return User(id, login, password, role)
    except:
        return None