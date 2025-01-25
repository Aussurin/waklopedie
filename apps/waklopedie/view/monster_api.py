from flask_restful import Resource
from flask import request

class MonsterAPI(Resource):
    
    def get(self):
        return  'machin'  # Le nom doit correspondre
       
    def put(self):

        return 'truc'
    
    def post(self):
        return  'TEST'  # Le nom doit correspondre
    
    def post(self):
        return  'TEST'  # Le nom doit correspondre