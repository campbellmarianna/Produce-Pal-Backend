import sqlite3
from flask import Flask, request, render_template
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity


class Market(Resource):
    parser = reqparse.RequestParser()
    #req parser reqiures certiain field to be true before they are inputed into database
    parser.add_argument('Adress',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

#get used to retrive data
    @jwt_required()
    def get(self, name):
        market = self.find_by_name(name)
        if market:
            return market
        return{'message': 'Market not found'}, 404

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM markets WHERE Name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return{'market': {'Name': row[1], 'adress': row[2]}}

#post sends data to backend only
    def post(self, name):
        if self.find_by_name(name):
            return{'message': "A market with name '{}' already exists.".format(name)},400

        data = Market.parser.parse_args()
        #inputs
        market = {'Name':name, 'Adress': data['Adress']}
        try:
            self.insert(market)
        except:
            return {'message': "An error occured inserting the data."}, 500

        return market, 201 #201 = created

    @classmethod
    def insert(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO markets VALUES (?, ?)"
        cursor.execute(query, (market['Name'], market['Adress']))

        connection.commit()
        connection.close()

    @jwt_required()
    def put(self, name):
        data = Market.parser.parse_args()

        market = self.find_by_name(name)
        updated_market = {'name': name, 'Adress': data['adress']}

        if market is None:
            try:
                self.insert(updated_market)
            except:
                return {'message': "An error occured inserting the data."}, 500

        else:
            try:
                self.update(updated_item)
            except:
                return {'message': "An error occured updateing the data."}, 500
        return updated_item

    @jwt_required()
    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM markets WHERE Name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()

        connection.commit()
        connection.close()

        return {'message': "Item Deleted"}

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE {table} SET Adress=? WHERE name=?"
        cursor.execute(query, (market['Adress'], market['Name']))

        connection.commit()
        connection.close()

#Index route turned into a class
class Marketlist(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM markets"
        cursor.execute(query)
        items = []
        for row in result:
            items.append({'name': row[1], 'adress': row[2]})
        connection.close()
        return {'markets': markets}
