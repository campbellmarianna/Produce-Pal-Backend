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


app.run(port = 5000, debug=True)
