from flask_restful import Resource

habilidades = {"Linux", "Windows", "Python", "Flask"}
class Habilidades(Resource):
    def get(self):
        return habilidades