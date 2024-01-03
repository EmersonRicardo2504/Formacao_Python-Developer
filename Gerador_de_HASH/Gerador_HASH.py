import hashlib      # importando livraria

#   solicitando mensagem pra cryptografia
string = input("Digite o texto a ser gerado o Hash: ")

#   menu para que seja escolhida a encriptação
menu = int(input('''### Esolha o tipo de HASH: ###
                        1) MD5 
                        2) SHA1
                        3) SHA256
                        4) SHA512
                        Escolha um HASH a ser gerado: '''))


#   estrutura de decisão com impressão da encryptação escolhida
if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print('A hash string é:', resultado.hexdigest())

elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print('A hash string é:', resultado.hexdigest())

elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print('A hash string é:', resultado.hexdigest())

elif  menu == 4:
    resultado = hashlib.sha512(string.endeco('utf-8'))
    print('A hash string é:', resultado.hexdigest())

else:
    print('Algo deu errado.')
