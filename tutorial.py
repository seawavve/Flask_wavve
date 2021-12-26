from flask import Flask,request
from flask_restx import Resource, Api
import numpy as np

app = Flask(__name__)
api = Api(app)


@api.route('/hello/<string:name>')
class Hello(Resource):
    def get(self, name):
        return {"message" : "Welcome, %s!" % name}

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
