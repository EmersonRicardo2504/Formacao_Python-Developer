# relizando importação
from models import Pessoas, db_session, Usuarios


#  criando funções

# realiza inserção de pessoas na tabela
def insere_pessoas():
    pessoa = Pessoas(nome='Emerson', idade=23)
    print(pessoa, 'incluida com sucesso')
    pessoa.save()

#  consulta pessoas na tabela
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas, 'consulta feita com sucesso')
    # pessoa = Pessoas.query.filter_by(nome='Emerson')
    # print(pessoa.idade)

# altera pessoas na tabela
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Emerson').first()
    pessoa.nome = 'Ricardo'
    pessoa.save()


# exclui pessoa da tabela
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Emerson').first()
    # pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


# faz chamada das funções
if __name__ == '__main__':
    insere_usuario('teste', '1234')
    insere_usuario('teste_02', '4321')
    consulta_todos_usuarios()
    # insere_pessoas()
    # altera_pessoa()
    # exclui_pessoa()
    # consulta_pessoas()
