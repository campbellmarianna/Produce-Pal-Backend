import sqlite3
from flask import Flask, request, render_template
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
from models.market import MarketModel


class Market(Resource):
    """ this is our market resource API"""
    TABLE_NAME = 'markets'

    parser = reqparse.RequestParser()
    #req parser reqiures certiain field to be true before they are inputed into database
    parser.add_argument('location',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

#get used to retrive data
    # @jwt_required()
    def get(self, name):
        market = MarketModel.find_by_name(name)
        if market:
            return market.json()
        return{'message': 'Market not found'}, 404

#post sends data to backend only
    def post(self, name):
        if MarketModel.find_by_name(name):
            return{'message': "A market with name '{}' already exists.".format(name)},400

        data = Market.parser.parse_args()
        #inputs
        market = MarketModel(name, data['location'])
        try:
            market.insert()
        except:
            return {'message': "An error occured inserting the data."}, 500
        return market.json(), 201 #201 = created

    # @jwt_required()
    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM {table} WHERE name=?".format(table=self.TABLE_NAME)
        result = cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {'message': "Item Deleted"}

    # @jwt_required()
    def put(self, name):
        data = Market.parser.parse_args()

        market = MarketModel.find_by_name(name)
        updated_market = MarketModel(name, data['location'])
        print("test1")

        if market is None:
            try:
                updated_market.insert()
            except:
                return {'message': "An error occured inserting the data."}, 500
        else:
            try:
                updated_market.update()
            except:
                return {'message': "An error occured updateing the data."}, 500
        return updated_market


#Index route turned into a class
class Marketlist(Resource):
    TABLE_NAME = 'markets'

    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        result = cursor.execute(query)
        markets = []
        for row in result:
            markets.append({'name': row[0], 'location': row[1]})
        connection.close()

        return {'markets': markets}
