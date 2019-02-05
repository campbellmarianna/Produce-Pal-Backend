import sqlite3
from flask import Flask, request, render_template
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT



class Market(Resource):
    parser = reqparse.RequestParser()
    #req parser reqiures certiain field to be true before they are inputed into database
    parser.add_argument('location',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

#get used to retrive data
    def get(self, name):
        connection = sqlite3.commect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM markets WHERE Name=?"




        market = next(filter(lambda x: x['name']==name, markets), None)
        return {'market': market},200 if market else 404 #404: Not Found

#post sends data to backend only
    def post(self, name):
        #Check to see if item in database and return error if it is
        if next(filter(lambda x: x['name'] == name, markets), None):
            return{'message': "An item with name '{}' already exists.".format(name)}, 400 #400: Bad Request
        data = Market.parser.parse_args()
        #inputs
        market = {'name':name, 'location': 'oakland'} #testing
        # market = {'name':name, 'location': data['location']} #should be used when request goes live
        #append to markets list
        markets.append(market)
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
