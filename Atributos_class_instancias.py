
# definindo a class 
class Estudante():

    #variavel que se alterada muda o comportamento da class por complete 
    escola = "Dio.me"

    def __init__(self, nome, matricula):
        self.nome = nome 
        self.matricula = matricula 
        

    def __str__(self) -> str:
        return f'{self.nome} - {self.matricula} - {self.escola}'
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
    


# realizando impressão de dados 
print('\t\nexemplo 1')
estudante_1 = Estudante("Emerson", 5)
print(estudante_1)

estudante_2 = Estudante("teste", 1)
print(estudante_2)

# consigo também definir uma função onde eu possa imprimir meus valores de forma diferente
# do primeiro exemplo 
print('\t\nExemplo 2 ')
mostrar_valores(estudante_1, estudante_2)