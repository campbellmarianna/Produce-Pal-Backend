import sqlite3

class MarketModel:

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
