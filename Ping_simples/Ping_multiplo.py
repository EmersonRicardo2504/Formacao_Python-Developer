import os
import time


with open('Host.txt') as file: # atribuindo variavel para leitura de ping
    dump = file.read()
    dump = dump.splitlines()

    print(dump)

    for ip in dump:

        print('Verificando o IP: ', ip)
        print("-"*60)

        os.system('ping -n 2 {}'.format(ip))
        print("-"*60)

        time.sleep(5) # definindo tempo de execução

