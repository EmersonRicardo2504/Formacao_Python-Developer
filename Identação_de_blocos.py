def sacar (valor):
    saldo = 500
    
    if saldo >= valor:
        print("valor sacado")
        print("Brigado por ser nosso cliente.\t")
        print("Volte sempre! ")

sacar(60)

def depositar(valor):
    saldo = 500 
    valor_sacado = int(input("Valor a ser sacado "))
    if saldo > valor_sacado:
        print("Saque autorizado. ")
    else:
        print("Tente novamente. ")

depositar(500)