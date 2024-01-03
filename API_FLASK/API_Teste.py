# 1 - importando bibliotecas
from flask import Flask

# 2 - definindo trafego
# 3 - variavel nome da aplicação

app = Flask(__name__)

# passando decorador
@app.route("/<numero>", methods=['GET','POST'])

# passando função
def ola(numero):

    # retornando impressão no site
    return "Teste feito com exito. {}".format(numero)

# nomeando para chamada
if __name__ == '__main__':
    app.run(debug=True)





