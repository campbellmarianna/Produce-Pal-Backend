import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegester(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be left blank!")
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be left blank!")

    def post(self):
        data = UserRegester.parser.parse_args()
        username = data.get('username', None)
        if not username:
            return {"message": "Username not found."}
        if UserModel.find_by_username(data['username']):
            return {"message":"A user with that name already exists."}

        user = UserModel(**data)
        user.save_to_db()

        return{"message": "user created successfully."}, 201
