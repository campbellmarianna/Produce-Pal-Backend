from werkzeug.security import safe_str_cmp
from models.user import UserModel
from flask_jwt import JWT


# @JWT.authentication_handler
def authenticate(username, password):
    print("test1**************")
    user = UserModel.find_by_username(username)
    print("test2**************")
    if user and safe_str_cmp(user.password, password):
        return user

# @JWT.identity_handler
def identity(payload):
    print("ID TEST **********************")
    user_id = payload['identity']
    return UserModel.find_by_id(user_id, None)
