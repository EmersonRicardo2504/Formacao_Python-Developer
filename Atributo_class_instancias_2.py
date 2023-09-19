
# definindo a class 
class Pessoa():

    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade 

    # dessa forma consigo consigo montar uma class dentro de outra class 
    @classmethod
    def criar_de_nascimento(cls, ano, mes, dia, nome):
        idade = 2023 - ano
        return cls(nome, idade)
    
    # metodo estatico de class 
    @staticmethod
    def maior_de_idade(idade):
        return idade >= 18
    

# impressão dos dados
p = Pessoa.criar_de_nascimento(2000, 4, 25, "Teste")
print(p.nome, p.idade)

print(Pessoa.maior_de_idade(18))
print(Pessoa.maior_de_idade(8))