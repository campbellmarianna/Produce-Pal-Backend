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

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUES (NULL, ?, ?)".format(table=self.TABLE_NAME)
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return{"message": "user created successfully."}, 201
