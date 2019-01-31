#Flask
from flask import Flask, request
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
    return "Hello World"


app.run(port = 5000, debug=True)
