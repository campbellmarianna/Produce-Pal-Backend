import sqlite3
from flask import Flask, request, render_template
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT



class Market(Resource):
    parser = reqparse.RequestParser()
    #req parser reqiures certiain field to be true before they are inputed into database
    parser.add_argument('Adress',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

#get used to retrive data
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
        market = {'Name':name, 'location': data['Adress']}
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO markets VALUES (?, ?)"
        cursor.execute(query, (market['Name'], market['Adress']))

        connection.commit()
        connection.close()

        return market, 201 #201 = created


    def put(self, name):

        data = Market.parser.parse_args()
        market = next(filter(lambda x: x['name'] == name, markets), None)
        if market is None:
            market = {'name': name, 'location': data['location']}
            markets.append(market)
        else:
            market.update(data)
        return market

    def delete(self, name):
        #filter out item to delete and create a new list
        # without that item overwriten to list name
        global markets
        markets = list(filter(lambda x: x['name'] != name, markets))
        return {'message': 'market deleted'}

#Index route turned into a class
class Marketlist(Resource):
    def get(self):
        return {'markets': markets}
