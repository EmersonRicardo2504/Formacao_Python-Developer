### Exemplo 1 - FOR sendo usado como interável 
texto = input("Informe um texto: ")
vagais = "AEIOU"

for letra in texto:
    if letra.upper() in vagais:
        print(letra, end= " ")
else: 
    print() 


### Exemplo 2 - range sendo usado com for
for numero in range(0, 11):
    print(numero, end= " ")

### Exemplo 3
for numero in range(0, 51, 5):
    print(numero, end= " ")


