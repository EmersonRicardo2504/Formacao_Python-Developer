
### Funções - exemplo 1 - montando e aplicando atualizações por posição e chave ###
print("\t\n### Funções - exemplo 1 - montando e aplicando atualizações a função ###\n")
def montando_carro(modelo, ano, placa, / , marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

montando_carro("Palio", 1999, "ABC-0505", marca = "Fiat", motor = "1.5", combustivel = "Gasolina")


### Funções - exemplo 1 - montando e aplicando atualizações por posição e chave ###
print("\t\n### Funções - exemplo 2 - montando e aplicando atualizações a função ###\n")
def teste(teste_1, teste_2, teste_3, / , teste_4, teste_5):
    print(teste_1, teste_2, teste_3, teste_4, teste_5)

teste("teste_1.1", "teste_2.2", "teste_3.3", teste_4= "teste_4.4", teste_5 = "teste_5.5")

### Funções - exemplo 3 - montando e aplicando atualizações a função ###
print("\t\n### Funções - exemplo 3 - montando e aplicando atualizações a função ###\n")

def moto(marca, cor, / , modelo, velocidade):
    print(marca, cor, modelo, velocidade)

moto("Yahama", "Branca", modelo = "Xt660", velocidade= 220)
moto("Kawasaki", "Verde", modelo = "HDR", velocidade= 399)
moto("Kawasaki", "Preta", modelo = "HDR-2", velocidade= 399)

### Funções - exemplo 5 - operando funções calculadora ###
print("\t\n### Funções - exemplo 5 - operando funções ###\n")

def divisão(a,b):
    return a / b

def subtração(a, b):
    return a - b 

def soma(a, b):
    return a + b

def multiplicação(a, b):
    return a * b

### ressultados


def resultado_divisão(a, b, função):
    resultado_operação = função(a, b)
    print(f"resulçtado da operação {a} / {b} = {resultado_operação}")

def resultado_multiplicação(a, b, função):
    resultado_operacao = função(a,b)
    print(f'resultado da operação {a} * {b} = {resultado_operacao}') 

def resultado_soma(a, b, função):
    resultado_operação = função(a, b)
    print(f"resultado da operação {a} + {b} = {resultado_operação}")

def resultado_subrtração(a, b, função):
    ressultado_operação = função(a, b)
    print(f"resultado da operação {a} - {b} = {ressultado_operação}")

resultado_multiplicação(5, 5, multiplicação)
resultado_soma(4, 4, soma)
resultado_subrtração(3, 2, subtração)
resultado_divisão(10, 5, divisão)

### Funções - exemplo 6 - operando funções ###
print("\t\n### Funções - exemplo 5 - operando funções ###\n")
salario = 2000

def bonus_salario(bonus):
    global salario 
    salario += bonus
    return salario

print(bonus_salario(1))