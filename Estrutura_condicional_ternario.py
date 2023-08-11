saldo = 1000
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} no saque")
