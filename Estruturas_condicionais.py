#### Exemplo tendo somente if/else

saldo = 1000
saque = float(input("informe o valor: "))

if saque <= saldo:
    print("Saque realizado!")

else:
    print("Sem saque!")


#### Exemplo onde somente o if e utilizado 

Maior_de_idade = 18
idade = float(input("Informe sua idade: "))

if idade >= Maior_de_idade:
    print("Você pode tirar carta!")

if idade < Maior_de_idade:
    print("Você deve passar de maior. ")

#### Exemplo tempo if/elif/else

pode_se_matricular = 18
deve_aguardar_maior_idade = 17

aluno = input("Informe seu nome: ")
idade = float(input("Informe sua idade: "))

if idade >= pode_se_matricular:
    print("Pode se matricular!")

elif idade <= deve_aguardar_maior_idade :
    print("Você deve aguardar maior idade ")