import sqlite3
import traceback

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
    parser.add_argument('farm_id',
        type=int,
        required=True,
        help="Every market needs a farm id "
    )

#get used to retrive data
    def get(self, name):
        market = MarketModel.find_by_name(name)
        if market:
            return market.json()
        return{'message': 'Market not found'}, 404

#post sends data to backend only
    # @jwt_required()
    def post(self, name):
        print("test1")
        if MarketModel.find_by_name(name):
            return{'message': "A market with name '{}' already exists.".format(name)},400

        data = Market.parser.parse_args()
        print("test2")
        market = MarketModel(name, **data)
        try:
            market.save_to_db()
        except Exception:
            return {'message': f"An error occured inserting the data:\n{traceback.print_exc}"}, 500
        return market.json(), 201 #201 = created

    @jwt_required()
    def delete(self, name):
        market = MarketModel.find_by_name(name)
        if market:
            market.delete_from_db()
        return {'message': "market deleted"}

    @jwt_required()
    def put(self, name):
        data = Market.parser.parse_args()
        market = MarketModel.find_by_name(name)

        if market is None:
            market = MarketModel(name, **data)
        else:
            market.location = data['location']
        market.save_to_db()
        return market.json()


#Index route turned into a class
class Marketlist(Resource):
    def get(self):
        return {'markets': list(map(lambda market: market.json(), MarketModel.query.all()))}
