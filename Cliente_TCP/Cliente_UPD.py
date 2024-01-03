import socket       # importando função

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # gerando conexão pro dataframa UDP

print("Cliente socket criado com sucesso.")

host = 'localhost'
porta = 5433                    #criando porta
mensagem = 'Olá servidor!'      #criando mensagem


try:                            # tentando conexão

    print('Cliente:' + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('Cliente: ' + dados)


finally:
    print('Cliente: Fechando a conexão.')
    s.close()