import hashlib

arquivo_1 = 'Senha_01'
arquivo_2 = 'Senha_2'

#   definindo primeiro HASH
hash_1 = hashlib.new('ripemd160')
hash_1.update(open(arquivo_1, 'rb').read())

#   definindo segundo HASH
hash_2 = hashlib.new('ripemd160')
hash_2.update(open(arquivo_2, 'rb').read())

#   validando se HASHS são diferentes
if hash_1.digest() != hash_2.digest():
    print(f'O arquivo: {arquivo_1} é diferente do arquivo: {arquivo_2}')
    print('O HASH do arquivo Senha_01 é: ', hash_1.hexdigest())
    print('O HASH do arquivo Senha_2 é: ', hash_2.hexdigest())

else:
    print(f'O arquivo: {arquivo_1} é igual o arquivo: {arquivo_2}')
    print('O HASH do arquivo Senha_01 é: ', hash_1.hexdigest())
    print('O HASH do arquivo Senha_2 é: ', hash_2.hexdigest())

