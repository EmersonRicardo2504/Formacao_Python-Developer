import socket # importanado biblioteca API pra realacionamento
import sys # importanto biblioteca com fortes funções para o interpretador


def main(): # defininfo função


    try:       # passando parametros para conexão

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    except socket.error as e:       #parametro pra excessão
        print("A conexão falhou.")
        print("Erro: {}".format(e))
        sys.exit()

    print("Socket criado com sucesso.")


    # solicitando para o usuario informações sobre o Host

    HostAlvo = input("Digite o HOST ou IP a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")


    try:

        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente TCP conectado com sucesso no Host: " + HostAlvo + "e na Porta: " + PortaAlvo)
        s.shutdown(2)

    except socket.error as e:
        print("A conexão falhou ao tentar ligar no Host: " + HostAlvo + "e porta: " + PortaAlvo)
        print("Erro: {}".format(e))
        sys.exit()


if __name__ == "__main__":      # chamando função
    main()