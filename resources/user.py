import sqlite3
from flask_restful import Resource, reqparse

from models.user import UserModel


class UserRegester(Resource):
    TABLE_NAME = 'users'

    parser = reqparse.RequestParser()
    #req parser reqiures certiain field to be true before they are inputed into database
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

        if UserModel.find_by_username(data['username']):
            return {"Message":"A user with that name already exits"}

        user = UserModel(**data)
        user.save_to_db()

        return{"message": "user created successfully."}, 201
