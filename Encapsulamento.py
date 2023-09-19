

# criando class 
class Conta: 
    def __init__(self, nro_agencia, saldo=0): 
        
        self._saldo = saldo
        self.nro_agencia = nro_agencia
        
    # criando funções 
    def depositar(self, valor):
        self._saldo += valor 

    @property
    def sacar(self, valor):
        self._saldo -= valor 


    def mostrar_saldo(self):
        return self._saldo

          


# atribuindo variável
conta = Conta('001', 100)


conta.depositar(100)
# conta.agencia("0001")

# impressão das informações -> funções 
print(conta.nro_agencia) # --> dessa forma chamo o argumento sem necessariamente 
                            # ele estar definido como função.


print(conta.mostrar_saldo()) # --> assim posso fazer a impressão da função







# conta.depositar(100000)
# print(conta.mostar_saldo())

# conta.sacar(50)
# print(conta.mostar_saldo())



