import socket       # definindo chamada da biblioteca

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado com sucesso.')

host = 'hostlocal'
port = 5432

s.bind((host, port))
mensagem = 'Servidor: Olá cliente!'


while 1:

    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem.')
        s.sendto(dados + (mensagem.encode()), end)

