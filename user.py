import sqlite3
from flask_restful import Resource, reqparse


class User(Resource):
    """our basic user template"""
    TABLE_NAME = 'users'

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        """returns users data by query"""
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE username=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row) # *row makes it the name is the rows in the init (excluding self)
        else:
            user = None

        connection.close()
        return user


    @classmethod
    def find_by_id(cls, _id):
        """Returns data by user_id"""
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE id=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user


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
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUES (NULL, ?, ?)".format(table=self.TABLE_NAME)
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return{"message": "User created successfully."}, 201
