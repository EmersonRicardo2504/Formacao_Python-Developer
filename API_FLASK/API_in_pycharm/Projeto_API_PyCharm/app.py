# importando bibliotecas
from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades, Usuarios
from flask_httpauth import HTTPBasicAuth

#  realizando criação das variaveis app e API
auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

# USUARIOS = {
#     'Emerson': '123',
#     'Ricardo': '321'
# }


# criando medoto de verificação para o autenticar

# @auth.verify_password # assim posso pedir autenticação pela senha
# def verificacao(login, senha):
#
#     if not (login, senha):
#         return False
#
#     return USUARIOS.get(login) == senha

@auth.verify_password # assim posso pedir autenticação pela senha
def verificacao(login, senha):

    if not (login, senha):
        return False

    return Usuarios.query.filter_by(login=login, senha=senha).first()


# realizando a criação da classe segundo o model
class Pessoa(Resource):
    @auth.login_required # assim posso pedir autenticação pelo login
    def get(self, nome):
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first()
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id

            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa não encontrada'

            }
        return response

    #     criando metodo pra realizar alterações
    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json

        # realizando função para alteração de dados nome
        if 'nome' in dados:
            pessoa.nome = dados['nome']

        # realizando função para alteração de dados idade
        if 'idade' in dados:
            pessoa.idade = dados['idade']

        #         forma para salvar alterações e commitalas
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response

    #     realizando inclusão da DEF delete
    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = 'Pessoa {} excluida com sucesso'.format(pessoa.nome)
        pessoa.delete()
        return {'status': 'suecesso', 'mensagem': mensagem}


# class pra listar registros
class Listapessoa(Resource):
    @auth.login_required
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade} for i in pessoas]
        return response

    #     função para inserir pessoas

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response


class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'pessoa': i.pessoa.nome} for i in atividades]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.nome,
            'nome': atividade.nome,
            'id': atividade.id
        }
        return response


# realizando criação de rota
api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(Listapessoa, '/pessoa/')
api.add_resource(ListaAtividades, '/atividade/')

#  criando operação para rodar app em modo Debug
if __name__ == '__main__':
    app.run(debug=True)
