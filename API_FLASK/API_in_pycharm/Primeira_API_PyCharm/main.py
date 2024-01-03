# 1 - importando bibliotecas
from flask import Flask, jsonify, request
import json

# 2 - defindo variavel
app = Flask(__name__)

# 3 - defindo rota e passando tipagem
@app.route('/<int:id>')

# 4 - definindo função
def pessoas(id):
    return jsonify({'id': id, 'nome':'Neno', 'profissao':'Atendente'})

# @app.route('/soma/<int:valor_1>/<int:valor_2>')
# def soma(valor_1, valor_2):
#     return jsonify({'soma' : valor_1 + valor_2})


# realizando inserção de informações pelo modo POST
@app.route('/soma', methods=['POST'])
def soma():

    if request.method == "POST":
        dados = json.loads(request.data)
        print(dados)
        total = sum(dados['valores'])

    elif request.method == 'GET':
        total = 10 + 10

    return jsonify({'soma': total})

# 5 - passando chamada
if __name__ == '__main__':
    app.run(debug=True)



