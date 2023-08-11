nome = "Emerson"
idade = 23 
profissao = "Programador"
linguagem = "Python"
saldo = 45.010


## formatando com .format

print("Olá me chamo {}, eu tenho {} idade. Trabalho como {} com a linguagem {}".format(nome, idade, profissao, linguagem))

print("Olá me chamo {nome}, eu tenho {idade} idade. Trabalho como {profissao} com a linguagem {linguagem}".format(nome=nome,
                                                                                                                  idade=idade,
                                                                                                                  profissao=profissao, 
                                                                                                                  linguagem=linguagem))

print(f"Olá me chamo {nome}, eu tenho {idade} idade. Trabalho como {profissao} com a linguagem {linguagem}")


## formatando com indice
print("Olá me chamo {0}, eu tenho {1} idade. Trabalho como {2} com a linguagem {3}".format(nome, idade, profissao, linguagem))


## formatando com %
print("Olá me chamo %s, eu tenho %d idade. Trabalho como %s com a linguagem %s" % (nome, idade, profissao, linguagem))

print(f"Olá me chamo {nome}, eu tenho {idade} idade. Trabalho como {profissao} com a linguagem {linguagem} ganho um total de {saldo:.1f}")

