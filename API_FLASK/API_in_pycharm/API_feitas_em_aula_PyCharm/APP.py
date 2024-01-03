# 1 - instalanddo bibliotecas
from flask import Flask, jsonify, request
import json

# 2 - criar variavel
app = Flask(__name__)

# criando as variaveis///dados em json
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


# 3 - passando rota
# devolve um desenvolvedor pelo ID, altera e deleta desenvolvedor
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
# 4 - dentro da rota passar informações
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]

        except IndexError:
            mensagem = 'Desenvolvedor com ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}

        except Exception:
            mensagem = 'Erro desconehcido, Procure o ADM da API'
            response = {'status': 'erro', 'mensagem': mensagem}

        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluido!'})


# lista de novos desenvolvedores e permiter registrar um desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def lista_dev():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])

    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)


