from flask_restful import Api
from apps.waklopedie.view.monster_api import MonsterAPI

def register_resources(app):
    api = Api(app)

    api.add_resource(MonsterAPI, '/waklopedie/monsters')