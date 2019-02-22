from flask import Flask, render_template
from flask_restful import Resource, Api
from flask_jwt import JWT
from markets import Market, Marketlist

#Inialize app
app = Flask(__name__)
api= Api(app)

#Hello world:

@app.route('/')
def home():
    world = "👽Hello Braus👽"
    return render_template("main.html", market = world)


#Call the method in the market class
api.add_resource(Market, '/market/<string:name>')
api.add_resource(Marketlist, '/markets')



if __name__ == '__main__':
    app.run(port = 5000, debug=True)
