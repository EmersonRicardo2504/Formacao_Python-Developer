#Dessa forma podemos separar infomações colocadas//solicitadas pelo user. 

nome = input("Informe seu nome: ")
sobrenome = input("Informe seu sobrenome: ")

print(nome, sobrenome)
print(nome,sobrenome, end= "...\n")
print(nome,sobrenome, sep= "#")