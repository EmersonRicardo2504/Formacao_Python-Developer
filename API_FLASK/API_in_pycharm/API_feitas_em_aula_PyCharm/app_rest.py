# 1- realizando importação das bibliotecas

from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
import json

# 2 -criando as variaveis
app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id': '0',
     'Nome': 'Emerson',
     'Profissao': 'Programador',
     'Habilidades': ['Python', 'Flask']
     },

    #     adicionando novos desenvolvedores

    {'id': '1',
     'Nome': 'Teste',
     'Profissao': 'Teste',
     'Habilidades': ['Teste_01', 'Teste_02']
     }
]


# 3- criando classes
class Desenvolvedor(Resource):

    # função para realizar chamada
    def get(self, id):

        try:
            response = desenvolvedores[id]

        except IndexError:
            mensagem = 'Desenvolvedor com ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}

        except Exception:
            mensagem = 'Erro desconehcido, Procure o ADM da API'
            response = {'status': 'erro', 'mensagem': mensagem}

        return response

    # função que função que nos possibilita inserir informações
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    # funções para que possamos realizar o delete
    def delete(self, id):

        desenvolvedores.pop(id)
        dados = json.loads(request.data)

        return {'status': 'sucesso', 'mensagem': 'Registro excluido.'}

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)
