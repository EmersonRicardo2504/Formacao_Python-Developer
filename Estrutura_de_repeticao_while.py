while True:
    numero = int(input("Informe um numero:"))
    
    if numero == 10: 
        break
    
    if numero % 2 == 10:
        continue

    print(numero)

for numero in range(100):
    if numero % 2 == 0:
        continue

    print(numero, end= " ")


    


 
