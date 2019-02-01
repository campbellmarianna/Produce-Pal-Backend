#Flask
from flask import Flask, request, render_template
#Import resource class from flask_restful
from flask_restful import Resource, Api
#Security features
from flask_jwt import JWT
#TODO create Security authentication


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
@app.route('/markets')
def index():
    # name = market["name"]
    # location = market["location"]
    return render_template("markets.html", name=market["name"], location=market["location"])

markets = []

class Market(Resource):
#get used to retrive data
    def get(self, name):
        #itterate over market list and return item
        market = next(filter(lambda x: x['name']==name, markets), None)
        return {'market': market},200 if market else 404 #404: Not Found

#post sends data to backend only
    def post(self, name):
        #Check to see if item in database and return error if it is
        if next(filter(lambda x: x['name'] == name, markets), None):
            return{'message': "An item with name '{}' already exists.".format(name)}, 400 #400: Bad Request
        data = request.get_json()
        #inputs
        market = {'name':name, 'location': 'oakland'} #testing
        # market = {'name':name, 'location': data['location']} #should be used when request goes live
        #append to markets list
        markets.append(market)
        return market, 201 #201 = created


    def put(self, name):
        pass

    def delete(self, name):
        #filter out item to delete and create a new list
        # without that item overwriten to list name 
        pass


#Call the method in the market class
api.add_resource(Market, '/market/<string:name>')



app.run(port = 5000, debug=True)
