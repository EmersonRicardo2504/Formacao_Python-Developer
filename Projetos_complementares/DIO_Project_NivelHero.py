'''
    Projeto DIO - level de XP do herói
'''

# Declarando valores das variaveis
ferro = 1000
bronze = 2000
prata = 5000
ouro = 7000
platina = 8000
ascendente = 9000
imortal = 1000
radiante = 10002

# Solicitando valores ao usuario

def consulta_XP():

    contador = 0
    print('*'*60)
    inicia_programa = int(input('Digite 1 pra iniciar e 0 pra parar o programa: '))
    while inicia_programa == 1:

        print('*' * 60)  # separador de linhas

        # Coletando dados - nome & XP
        nome = input('Coloque seu user: ')
        valorXP_perguntado = float(input("Coloque a sua xp: "))

        # Estrutura de decisão xp ferro
        if valorXP_perguntado <= ferro:
            print('{nome} sua XP atual é de: {valorXP_perguntado}'.format(
                valorXP_perguntado=valorXP_perguntado,
                nome=nome))

            # imprimindo valor a ser alcançado para o proximo level
            valorXP_proximoLevel = valorXP_perguntado - 1000
            print('{nome} para atingir outro nivel falta {valorXP_proximoLevel} XP'.format(
                nome=nome,
                valorXP_proximoLevel=valorXP_proximoLevel
            ))
            print("*" * 60)  # separador de linhas
            return

            # Estrutura de decisão xp Bronze
        if valorXP_perguntado <= bronze:
            print('{nome} sua XP atual é de: {valorXP_perguntado}'.format(
                valorXP_perguntado=valorXP_perguntado,
                nome=nome))

            # imprimindo valor a ser alcançado para o proximo level
            valorXP_proximoLevel = valorXP_perguntado - 2000
            print('{nome} para atingir outro nivel falta {valorXP_proximoLevel} XP'.format(
                nome=nome,
                valorXP_proximoLevel=valorXP_proximoLevel
            ))
            print("*" * 60)  # separador de linhas
            return

         # Estrutura de decisão xp Prata
        if valorXP_perguntado <= prata:
            print('{nome} sua XP atual é de: {valorXP_perguntado}'.format(
                valorXP_perguntado=valorXP_perguntado,
                nome=nome))

            # imprimindo valor a ser alcançado para o proximo level
            valorXP_proximoLevel = valorXP_perguntado - 5000
            print('{nome} para atingir outro nivel falta {valorXP_proximoLevel} XP'.format(
                nome=nome,
                valorXP_proximoLevel=valorXP_proximoLevel
            ))
            print("*" * 60)  # separador de linhas
            return

         # Estrutura de decisão xp Ouro
        if valorXP_perguntado <= ouro:
            print('{nome} sua XP atual é de: {valorXP_perguntado}'.format(
                valorXP_perguntado=valorXP_perguntado,
                nome=nome))

            # imprimindo valor a ser alcançado para o proximo level
            valorXP_proximoLevel = valorXP_perguntado - 7000
            print('{nome} para atingir outro nivel falta {valorXP_proximoLevel} XP'.format(
                nome=nome,
                valorXP_proximoLevel=valorXP_proximoLevel
            ))
            print("*" * 60)  # separador de linhas
            return

         # Estrutura de decisão xp Platina
        if valorXP_perguntado <= platina:
            print('{nome} sua XP atual é de: {valorXP_perguntado}'.format(
                valorXP_perguntado=valorXP_perguntado,
                nome=nome))

            # imprimindo valor a ser alcançado para o proximo level
            valorXP_proximoLevel = valorXP_perguntado - 8000
            print('{nome} para atingir outro nivel falta {valorXP_proximoLevel} XP'.format(
                nome=nome,
                valorXP_proximoLevel=valorXP_proximoLevel
            ))
            print("*" * 60)  # separador de linhas
            return

            # Estrutura de decisão xp Ascendente
        if valorXP_perguntado <= ascendente:
            print('{nome} sua XP atual é de: {valorXP_perguntado}'.format(
                valorXP_perguntado=valorXP_perguntado,
                nome=nome))

            # imprimindo valor a ser alcançado para o proximo level
            valorXP_proximoLevel = valorXP_perguntado - 9000
            print('{nome} para atingir outro nivel falta {valorXP_proximoLevel} XP'.format(
                nome=nome,
                valorXP_proximoLevel=valorXP_proximoLevel
            ))
            print("*" * 60)  # separador de linhas
            return

            # Estrutura de decisão xp Imortal
        if valorXP_perguntado <= imortal:
            print('{nome} sua XP atual é de: {valorXP_perguntado}'.format(
                valorXP_perguntado=valorXP_perguntado,
                nome=nome))

            # imprimindo valor a ser alcançado para o proximo level
            valorXP_proximoLevel = valorXP_perguntado - 10000
            print('{nome} para atingir outro nivel falta {valorXP_proximoLevel} XP'.format(
                nome=nome,
                valorXP_proximoLevel=valorXP_proximoLevel
            ))
            print("*" * 60)  # separador de linhas
            return

            # Estrutura de decisão xp Radiante
        if valorXP_perguntado >= radiante:
            print('{nome} sua XP atual é de: {valorXP_perguntado}'.format(
                valorXP_perguntado=valorXP_perguntado,
                nome=nome))

            # imprimindo valor a ser alcançado para o proximo level
            valorXP_proximoLevel = 'Nivel maximo alcançado parabens!'
            print('{nome} nivel maximo ultrapassado, parabéns!'.format(
                nome=nome,

            ))
            print("*" * 60)  # separador de linhas
            return


        break

# Chamada pra saida de dados
consulta_XP()