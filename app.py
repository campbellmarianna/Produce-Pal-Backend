#Flask
from flask import Flask, request, render_template
#Import resource class from flask_restful
from flask_restful import Resource, Api, reqparse
#Security features
from flask_jwt import JWT
#TODO create Security authentication
from markets import Market, Marketlist

#Inialize app
app = Flask(__name__)
api= Api(app)

#Hello world:

@app.route('/')
def home():
    world = "Hello World"
    return render_template("main.html", market = world)

#Model
# market = {
#     'market_id': 'M123',
#     'name': 'Alamany Farmers Market',
#     'location': '100 Alemany Blvd, San Francisco, CA 94110',
# }

# INDEX
# @app.route('/markets')
# def index():
#     # name = market["name"]
#     # location = market["location"]
#     return render_template("markets.html", name=market["name"], location=market["location"])

# markets = []


#Call the method in the market class
api.add_resource(Market, '/market/<string:name>')
api.add_resource(Marketlist, '/markets')



app.run(port = 5000, debug=True)
