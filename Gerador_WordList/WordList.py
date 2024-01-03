import itertools #  inportando biblioteca

#   solicitando padrão pra lista percorrer
string = input("String a ser transmultada: ")

#   estrutura pra que possamos ler entrada de dados e quantidade de dados
resultado = itertools.permutations(string, len(string))


# Gerando a lista de senha (WorList)
for i in resultado:
    print(''.join(i))


