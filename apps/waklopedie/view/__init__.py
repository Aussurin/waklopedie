from flask_restful import Api
from apps.waklopedie.view.monster_api import MonsterAPI
from apps.waklopedie.view.classe_api import ClasseAPI
from flask import request

def register_resources(app):
    api = Api(app)
    api.add_resource(MonsterAPI, '/waklopedie/monsters/')  # Vérifiez la cohérence avec Angular
    api.add_resource(ClasseAPI, '/waklopedie/classe/<id>')