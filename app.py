from flask import Flask, render_template
from flask_restful import Resource, Api
from markets import Market, Marketlist
from flask_jwt import JWT, jwt_required

#internal imports
from security import authenticate, identity


#Inialize app
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'alien'
api= Api(app)

jwt = JWT(app, authenticate, identity)

#Hello world:

@app.route('/')
def home():
    world = "Hello World"
    return render_template("main.html", market = world)


#Call the method in the market class
api.add_resource(Market, '/market/<string:name>')
api.add_resource(Marketlist, '/markets')


if __name__ == '__main__':
    app.run(port = 5000, debug=True)

app.run()
