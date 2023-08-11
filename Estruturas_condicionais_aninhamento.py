conta_normal =False
conta_universitaria = False
conta_especial = False


saldo = 1000
saque = 900
cheque_especial = 450

if conta_normal:
   
    if saldo >= saque:
        print("Saque realizado!")
    elif saque <= (saldo + cheque_especial):
        print("Saque feito com cheque especial!")
    else:
        print("Não foi possivel realizar o saque!")

elif conta_universitaria:
    
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Sem valor para sacar.")

elif conta_especial:
    print("Conta especial selecionada")

else:
    print("Nenhuma conta selecionada!")