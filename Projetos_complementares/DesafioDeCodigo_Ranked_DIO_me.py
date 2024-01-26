'''
    - Desafio de codigo - RanKed Dio.me
    - Autor: Emerson Rircardo
'''

# Declarando variaveis para comparações
ferro = 10
bronze = 20
prata = 50
ouro = 80
diamante = 90
lendario = 100
imortal = 101


# Criando função para realizar comparações
def ranked():
    print('*' * 60)  # impressão da borda
    # Perguntando se cliente deseja começar programa
    executar_programa = int(input(' 1 inicia o programa 0 encerra: '))
    while executar_programa == 1:  # estrutura de decição

        print('*' * 60)  # impressão da borda

        # Solicitando informações pro usuario nome/vitorias
        nome = input('Digite seu nome: ')
        vitorias = int(input('Coloque sua quantidade de vitorias: '))

        # Realizando crianção de estrutura de decição
        # Caso usuario seja ferro
        if vitorias <= ferro:
            print('{nome} você está no nível ferro com {vitorias} vitorias '.format(nome=nome, vitorias=vitorias))
            proximo_Level = vitorias - ferro
            print('{nome} faltam {proximo_Level} vitorias pra subir de ranked!'.format(nome=nome,
                                                                                       proximo_Level=proximo_Level))
            print('*' * 60)
            return

        # Caso usuario seja bronze
        if vitorias <= bronze:
            print('{nome} você está no nível bronze com {vitorias} vitorias '.format(nome=nome, vitorias=vitorias))
            proximo_Level = vitorias - bronze
            print('{nome} faltam {proximo_Level} vitorias pra subir de ranked!'.format(nome=nome,
                                                                                       proximo_Level=proximo_Level))
            print('*' * 60)
            return

        # Caso usuario seja prata
        if vitorias <= prata:
            print('{nome} você está no nível prata com {vitorias} vitorias '.format(nome=nome, vitorias=vitorias))
            proximo_Level = vitorias - prata
            print('{nome} faltam {proximo_Level} vitorias pra subir de ranked!'.format(nome=nome,
                                                                                       proximo_Level=proximo_Level))
            print('*' * 60)
            return

        # Caso usuario seja ouro
        if vitorias <= ouro:
            print('{nome} você está no nível ouro com {vitorias} vitorias '.format(nome=nome, vitorias=vitorias))
            proximo_Level = vitorias - ouro
            print('{nome} faltam {proximo_Level} vitorias pra subir de ranked!'.format(nome=nome,
                                                                                       proximo_Level=proximo_Level))
            print('*' * 60)
            return

        # Caso usuario seja diamante
        if vitorias <= diamante:
            print('{nome} você está no nível diamante com {vitorias} vitorias '.format(nome=nome, vitorias=vitorias))
            proximo_Level = vitorias - diamante
            print('{nome} faltam {proximo_Level} vitorias pra subir de ranked!'.format(nome=nome,
                                                                                       proximo_Level=proximo_Level))
            print('*' * 60)
            return

        # Caso usuario seja Lendario
        if vitorias <= lendario:
            print('{nome} você está no nível lendario com {vitorias} vitorias '.format(nome=nome, vitorias=vitorias))
            proximo_Level = vitorias - lendario
            print('{nome} faltam {proximo_Level} vitorias pra subir de ranked!'.format(nome=nome,
                                                                                       proximo_Level=proximo_Level))
            print('*' * 60)
            return

        # Caso usuario seja imortal
        if vitorias >= imortal:
            print('{nome} você está no nível imortal com {vitorias} vitorias '.format(nome=nome, vitorias=vitorias))
            print('{nome}, nivel maxímo alcançado, parabéns! '.format(nome=nome))
            print('*' * 60)
            return

        break


# Criando saida de dados
def main():
    ranked()


if __name__ == '__main__':
    main()
