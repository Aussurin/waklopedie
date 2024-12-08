from flask_restful import Resource

class MonsterAPI(Resource):

    def get(self):
        return "Hello World"