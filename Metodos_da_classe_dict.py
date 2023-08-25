### imprimindo informações simples atraves de um dicionario 
print("\n### exemplo 1 = imprimindo informações simples atraves de um dicionario ###\n")
info = {"Nome" : "Neno", "Telefone" : "123456-7890", "Endereço" : "Rua Frederick Voith"}
print(type(info))
print(info["Nome"])
print(info["Telefone"])
print(info["Endereço"])

### exemplo 2 - apagando dicionario .clear() ### 
print("\n### exemplo 2 - apagando dicionario ### ")
info_2 = {"Nome" : "Teste 1", "Telefone" : "123456-7890", "Endereço" : "Rua 000001 "}
print(type(info_2))
info_2.clear()
print(info_2)

### exemplo 3 - copiando dicionario .copy() ### 
print("\n### exemplo 3 - copiando dicionario .copy() ### \n")
info_3 = {"Nome" : "Teste 2", "Telefone" : "123456-7890", "Endereço" : "Rua 000002 "}
print(type(info_3))

copia = info_3.copy()
copia["Nome"] = {"Teste_3"}
copia["Telefone"] = {"012345-6789"}
copia["Endereço"] = {"000003"}

print(info_3)
print("\nAlteração realizada\n")
print(copia)

### exemplo 3.1 .copy()
print("\n### exemplo 3.1 .copy() ###\n")
info_t3 = {"emerson.ricardo153@gmail.com" : {"nome": "Emerson", "telefone": "94605-4378"}}

print(type(info_t3))
print(info_t3)

copia_t3 = info_t3.copy()
print("\nAlteração realizada.\n")
copia_t3["emerson.ricardo153@gmail.com"] = {"nome": "Ricardo", "telefone": "00000-0000"}
print(copia_t3)

print("\nAlteração no copy\n")
info_t4 = {"emerson.ricardo153@gmail.com" : {"nome": "Ricardo", "telefone": "00000-0000"}}
copia_t4 = info_t4.copy()
copia_t4["emerson.ricardo153@gmail.com"] = {"nome": "sucesso", "telefone": "sucesso" }
print(copia_t4)


 ### exemplo 4 - criar chaves com .fromkeys{[]} ###
print("\n### exemplo 4 - criar chaves com .fromkeys([]) ###\n")
teste = dict.fromkeys(["Teste", "Teste_2"])
print(teste)

print("\n### exemplo 4.1 - criar chaves com .fromkeys([]) ###\n")
info_4 = {"Nome" : "Teste 4", "Telefone" : "00000-0004", "Endereço" : "Rua 000004 "}
print(type(info_4))
print(info_4)

print("\nAlterações realizadas\n")
info_5 = info_4.fromkeys(["Nome", "Telefone", "Endereço"], "Teste_05")
print(info_5)

###  exemplo 5 - criando dicionario com .get() ###
print("\n### exemplo 5 - criando dicionario com .get() ###\n")
info_6 = {
    "teste@gmail.com": {"nome": "teste", "telefone": "00006-0000" }
}
#info_6["teste"]
#info_6.get(teste) ### em amabas as partes comentadas teriamos erros empressos
info_6.get("teste", {})
print(info_6)

print("\n###  exemplo 5.2 - criando dicionario com .get() ###\n")
info_6.get("teste@gmail.com", {})
print(info_6)

### exemplo 6 -  retornando chave com .keys() ###
print("\n### exemplo 6 -  retornado chave com .keys() ###\n")
info_7 = {
    "teste@gmail.com": {"nome": "teste", "telefone": "00006-0000" }
}
print(info_7.keys())

### exemplo 7 - eliminando chave com .pop() ### 
print("\n### exemplo 7 - eliminando chave com .pop() ###\n ")
info_8 = {
    "teste@gmail.com": {"nome": "teste", "telefone": "00006-0000" }
}
teste_info_8 = info_8.pop("teste@gmail.com", {})
print(teste_info_8)

teste_pop = info_8.pop("teste@gmail.com", {})
print(teste_pop)

### exemplo 8 - adicionando chave com .setdefault() ###
print("### exemplo 8 - adicionando chave com .setdefalt() ###")
info_9 = {
    "Exemplo": {"Teste1": "teste01", "teste2": "teste02"}
}
info_9.setdefault("teste3", "teste03")
print(info_9)






