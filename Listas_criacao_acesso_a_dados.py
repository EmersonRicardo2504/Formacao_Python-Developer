nome = list("Neno")
print(nome)


###################################

numeros = list(range(1, 10))
print(numeros)

###################################


frutas = [
    "maça",
    "banana",
    "uva",
    "melancia"
]
print(frutas[-1])
print(frutas[1])


####################################

matriz = [
    ["nome", "carro", 3],
    ["vinho", "dinheiro", 7],
    ["sorte", 8, "vida"]
]

print(matriz[2][:])
print(matriz[1][2])

#####################################


numbers = ["1", "2", "3", "4", "5"]

print(numbers[0:3:2])
print(numbers[0:4])

####################################################

carros = ["gol", "astra", "geep"]

#for carros in carros:
    #print(carros)

for indice, carros in enumerate(carros):
    print(f"{indice} : {carros}")

###############################################

n = [1,2,3,4,5,6,7,8,9]
pares = []
inpares = []

for teste in n:
    if teste % 2 == 0:
        pares.append(teste)
        print(pares)

    if teste % 2 == 1:
        inpares.append(teste)
        print(inpares)
        

        

        

