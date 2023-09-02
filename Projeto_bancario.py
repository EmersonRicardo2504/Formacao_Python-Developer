import textwrap

### Menu que será impresso para o usuario escolher função 
def menu():

    menu = ''' \n     \t### Menu ###
    [1]\tDepositar 
    [2]\tSaque 
    [3]\tExtrato
    [4]\tNova conta
    [5]\tLista contas
    [6]\tNovo usuário
    [0]\tSair
=> '''
    return input(textwrap.dedent(menu))

# def depositar
def depositar(saldo, valor, extrato, / ):
    
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\t\tR${valor:.2f}\n"
        print("\n ###### Desposito realizado com sucesso! ###### ")
    else:
        print("\n###### Operação falhou! O valor informado é invalido. ######")

    return saldo, extrato   

# def sacar
def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    
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
        extrato += f"Saque:\t\tR${valor:.2f}\n"
        numero_saques += 1
        print("\n### Saque realizado com sucesso! ###")

    else: 
        print("\n### Operação falhou o valor informado e invalido! ### ")

    return saldo, extrato 

# exibindo extrato 
def exibir_extrato(saldo, / , *, extrato):
    print("########## EXTRATO ##########")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\tR${saldo:.2f}")
    print("##############################")  

# criando usuário   
def criar_usuario(usuarios):
    cpf = input("Informe o cpf (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n###já existe usuario com esse CPF! ###")
        return

    nome = input("Informe o nome complete: ")
    data_nascimento = input("Informe seu nascimento (DD/MM/AA):")
    endereço =  input("Informe o endereço (Logradouro, nro - Bairro - cidade/sigla estado): ")

    usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereço })
    
    print("### Usuario criado com sucesso! ###")

#def filtrar usuario
def filtrar_usuario(cpf, usuarios):

    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

# def criar conta
def criar_conta(agencia, numero_conta, usuarios):

    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n### Conta criada com sucesso! ###")
        return {"agencia":agencia, "numero_conta": numero_conta, "usuario": usuario}
        
    print("\n### Usuario não encontrado, fluxo de criação encerrado! ###")

# def listar contas
def listar_contas(contas): 
    for conta in contas:
        linha = f'''\
        Agencia:\t{conta["agencia"]}
        C/C:\t\t{conta["numero_conta"]}
        Titular:\t{conta["usuario"]["nome"]}

'''
        print("=" * 100)
        print(textwrap.dedent(linha))



def main():

    LIMITE_SAQUES = 3 
    AGENCIA = "0001"
        
    saldo = 0
    limite = 500
    extrato = " "
    numero_saques = 0
    usuarios =  []
    contas = []

    while True:
       
        opcao = menu()
        
        # opção deposito        
        if opcao == "1":
            valor = float(input("Informe o valor do deposito: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
        
        # opção saque 
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques, 
            LIMITE_SAQUES=LIMITE_SAQUES,
            )
        
        # opção extrato    
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        
        # opção de criar conta
        elif opcao == "4":
            numero_conta = len(contas) +1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        # opção de listar contas 
        elif opcao == "5":
            listar_contas(contas)


        # opção criar usuario
        elif opcao == "6":
            criar_usuario(usuarios)


        # opção pra sair do programa  
        elif opcao == "0":
            break

        else:
            print("operação invalida, por favor selecione a operação desejada.")

main()
