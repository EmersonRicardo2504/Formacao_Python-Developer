### Funções. 

### exemplo 1 - def() ###
print("\n\t### exemplo 1 - def() ###\n")
def teste():
    print("Hello Word!")
print(teste())

### exemplo 2 - def() + format ###
print("\n\t### exemplo 2 - def() + format ###\n")
def teste_2(nome):
    print(f'Bem vindo {nome}!')

teste_2(nome="Emerson")


### exemplo 3 - def() + format ###
print("\n\t### exemplo 3 - def() + format ###\n")
def teste_3(nome="Teste"):
    print(f"Bem vindo {nome}!")
teste_3()


### Exemplo 4 - calculo com função ###
print("\n\t### Exemplo 4 - calculo com função ###\n")
def calcular_numeros(numeros):
    return sum(numeros)

print(calcular_numeros([10, 1, 9999]))


### Exemplo 5 - calculo antecessor e sucessor ###
print("\n\t### Exemplo 5 - calculo antecessor e sucessor ###\n")
def sucessor_e_antecessor(numero):
    
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(sucessor_e_antecessor(2))
print(sucessor_e_antecessor(5))
print(sucessor_e_antecessor(8))

### Exemplo 6 - ### Exemplo 5 - calculo antecessor e sucessor ###")
print("\n\t### Exemplo 6 - montadora ###\n")
def carros(modelo, marca, ano, placa):
    print(f"Carro inserido com sucesso {modelo}/{marca}/{ano}/{placa}")

carros("BMW", "M-4", 2000, "DEF-4321")
carros(marca="Fiat",modelo= "Palio", ano="1990", placa="ABC-1234")
carros(**{"marca": "Fiat","modelo": "fox", "ano": 2015, "placa": "HIJ-7894" })