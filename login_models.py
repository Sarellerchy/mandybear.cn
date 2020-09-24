from flask_login import UserMixin

class User(UserMixin):
    pass

users = [
    {'id':'mandybear', 'username': 'mandybear', 'password': 'qwer1234'}
]

def query_user(user_id):
    for user in users:
        if user_id == user['id']:
            return user