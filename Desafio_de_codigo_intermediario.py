exemplo = '''
A primeira linha contém um número inteiro C relativo ao número de casos de teste. 
Em seguida, haverá C linhas, com um número inteiro N (100 <= N <= 100000) 
Relativo ao nível de energia de um ser vivo

Leia as as entradas e crie as condições necessárias para verificar se é maior ou
    menor do que 8000 e imprima "Inseto!" ou "Maior que 8000!" para cada caso.
           
'''

print(exemplo)

C = int(input("Coloque o valor indentificado:"))

for _ in range (C): 
    if C <= 8000:
        print("Inseto!")

    else:
        print("Mais de oito 8000 possivel dragão identificado! ")
        print("Perigo!")

    break


