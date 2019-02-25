import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = ('users')
    """our basic user template"""

    id = db.Column(db.Integer, primary_key=True)
    username = db.column(db.String(80))
    password = db.column(db.String(80))


    def __init__(self, id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        """returns users data by query"""
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
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

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user
