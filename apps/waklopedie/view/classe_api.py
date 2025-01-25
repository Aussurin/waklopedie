from flask_restful import Resource
from mongoengine import *
from ..model.classe import Classe

class ClasseAPI(Resource):

    def get(self, id):
        
        classe = Classe.objects(name__iexact=id)
        return classe
    
    def put(self):
        
        return 'patate'

    def patch(self):
        return "Hello World"

    def post(self):
        return "Hello World"

    def delete(self):
        return "Hello World"

    