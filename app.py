import os # gives us access to operating system environment variables

from flask import Flask, render_template
from flask_restful import Api
from flask_jwt import JWT
# from dotenv import load_dotenv
# import os

from db import db
from security import authenticate, identity
from resources.user import UserRegester
from resources.markets import Market, Marketlist
from resources.farm import Farm, FarmList
from models.user import UserModel


#Inialize app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
# app.config['JWT_AUTH_USERNAME_KEY'] = 'joy'
# app.config['JWT_AUTH_PASSWORD_KEY'] = 'asdf'

app.secret_key = 'jose'

# app.secret_key = load_dotenv(SECRET_KEY)
api= Api(app)

jwt = JWT(app, authenticate, identity) #/auth

# help(JWT)

@app.before_first_request
def create_tables():
    db.create_all()


#Hello world:
@app.route('/')
def home():
    world = "👽Hello Braus👽"
    return render_template("main.html", market = world)


#Call the method in the market class
api.add_resource(Farm, '/farm/<string:name>')
api.add_resource(Market, '/market/<string:name>')
api.add_resource(FarmList, '/farms')
api.add_resource(Marketlist, '/markets')
api.add_resource(UserRegester, '/regester')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port = 5000, debug=True)
