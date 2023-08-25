### Formas de criar um dicionario
print("\n######### Exemplo 1 ##########\n")

pessoa = {"nome" : "Neno", "idade": 23}
print(pessoa)

pessoa_2 = dict(nome= "Lurdes", idade = 53)
print(pessoa_2)

### Acrecentando informação a variavel pessoa_2
print("\n######### exemplo 2 ##########\n")

pessoa_2["Telefone"] = "12345-6789"
print(pessoa_2)

### formas de imprimir a chave

print("\n######### exemplo 4 ##########\n")

dados = {"Nome" : "Emerson", "Idade: " : 23, "telefone" : "12345-6789"}
print(dados["Nome"])
print(dados["Idade: "])
print(dados["telefone"])

### modificando valor na chave 
print("\n######### Modicação realizada exemplo 4 ##########\n")

dados["Nome"] = "Ricardo"
dados["Idade: "] = 24
dados["telefone"] = "98765-4321"

print(dados["Nome"])
print(dados["Idade: "])
print(dados["telefone"])

### exemplo 5 acessando dicionario

print("\n###### exemplo 5 acessando dicionario ######\n")

email = {

    "teste@gmail.com" : {"nome" : "Emerson", "telefone" : "123456-7890"},
    "teste2@gmail.com" : {"nome" : "Luan", "telefone" : "987456-1230"},
    "teste3@gmail.com" : {"nome" : "Geraldo", "telefone" : "157411-36955", "teste" : "Sucesso"}
}

contato = email["teste@gmail.com"]["telefone"]
print(contato)

contato_2 = email["teste2@gmail.com"]["telefone"]
print(contato_2)

contato_3 = email["teste3@gmail.com"]["teste"]
print(contato_3)

### exemplo 6 com for in:
print("\nexemplo 6 com for in: \n")
info = {

    "teste@gmail.com" : {"nome" : "Emerson", "telefone" : "123456-7890"},
    "teste2@gmail.com" : {"nome" : "Luan", "telefone" : "987456-1230"},
    "teste3@gmail.com" : {"nome" : "Geraldo", "telefone" : "157411-36955"}
}

for informações in info:
    print(informações, info[informações])

print("\nexemplo 7 com for in: \n")
for informações, valor in info.items():
    print(informações, valor)


    

