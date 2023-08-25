

menu = '''
    [1] Deposito 
    [2] Saque 
    [3] Extrato
    [4] Sair
=> '''

print(menu)

saldo = 0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:2f}\n"

        else:
            print("Operação falhou! O valor é invalido. ")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite 
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo o sufuciente. ")

        elif excedeu_limite:
            print("O valor do saldo excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Numero de saque excedidos. ") 

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else: 
            print("Operação falhou! O valor informado é invalido.  ")   


    elif opcao == "3":
        print("########## EXTRATO ##########")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("##############################")

    elif opcao == "4":
        break

    else:
        print("operação invalida, por favor selecione a operação desejada.")