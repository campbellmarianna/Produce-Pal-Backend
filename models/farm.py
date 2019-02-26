import sqlite3
from db import db

class MarketModel(db.Model):
    __tablename__='markets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    location = db.Column(db.String(300))


    def __init__(self, name, location):
        self.name = name
        self.location = location

    def json(self):
        return {'name': self.name, 'location': self.location}

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM markets WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return cls(*row)

    def insert(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO markets VALUES (?, ?)"
        cursor.execute(query, (self.name, self.location))

        connection.commit()
        connection.close()

    def update(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE markets SET location=? WHERE name=?"
        cursor.execute(query, (self.location, self.name))

        connection.commit()
        connection.close()
