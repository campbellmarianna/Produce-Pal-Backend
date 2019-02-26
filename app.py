from flask import Flask, render_template
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
from resources.user import UserRegester
from resources.markets import Market, Marketlist
from resources.farm import Farm, FarmList


#Inialize app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #tells SQL alcamy that the DB is in our root file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.secret_key = 'alien'
api= Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

# jwt = JWT(app, authenticate, identity)

#Hello world:
@app.route('/')
def home():
    world = "Hello Braus"
    return render_template("main.html", market = world)


#Call the method in the market class
api.add_resource(Farm, '/farm/<string:name>')
api.add_resource(Market, '/market/<string:name>')
api.add_resource(FarmList, '/farms')
api.add_resource(Marketlist, '/markets')
api.add_resource(UserRegester, '/regester')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port = 5000, debug=True)
