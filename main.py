from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

class status(Resource):    
     def get(self):
         try:
            return {'data': 'Api running'}
         except(error): 
            return {'data': error}

class Sum(Resource):
    def get(self, a, b):
        return jsonify({'data': a+b})

api.add_resource(status, '/')
api.add_resource(Sum,'/add/<int:a>,<int:b>')

if __name__ == '__main__':
    app.run()