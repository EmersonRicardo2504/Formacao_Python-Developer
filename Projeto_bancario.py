import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereço):
        self.endereço = endereço
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta) 

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereço):
        super().__init__(endereço)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:

    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero 
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico() 
      

    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property 
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia 
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    

    # def sacar
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
       
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo o sufuciente. ")
        
        elif valor > 0:
            self._saldo -= valor
            print("\n### Saque realizado com sucesso! ###")
            return True
        
        else: 
            print("\n### Operação falhou o valor informado e invalido! ### ")
    
        return False 
        
    def depositar(self, valor):
        if valor > 0: 
            self._saldo += valor 
            print("\n### Deposito realizado com sucesso! ")

        else: 
            print("\n### Operação falhou! O valor informado é invalido. ###")
            return False 
        
        return True

class ContaCorrente:
    def __init__ (self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite 
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.
            transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        execedeu_saques = numero_saques >= self._limite_saques ####

        if excedeu_limite:
            print("###\tOperação falhou! O valor do saque excedeu o limite.\t###")

        elif execedeu_saques:
            print("\n###\tOperação falhou! Numero de saques excedido.\t###")

        else:
            return super().sacar(valor)
        
        return False 

    def __str__(self):
        return f"""\ 
        Agencia:\t{self.agencia}
        C\C:\t\t{self.numero}
        Titular:\t{self.cliente.nome}
        """
    
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__, 
                "valor": transacao.valor,
                "data": datetime.now().strftime
                ("%d-%m-%Y %H:%M:%s" ),
            }
        )

class Transacao(ABC):
    
    @property
    @abstractproperty
    def valor(self):
        pass 

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):

    def __init__(self,valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
        def __init__(self, valor):
            self._valor = valor

        @property
        def valor(self):
            return self._valor
        
        def registar(self, conta):
            sucesso_transacao = conta.depositar(self.valor)

            if sucesso_transacao:
                conta.historico.adicionar_transacao(self)







### Menu que será impresso para o usuario escolher função 
def menu():

    menu = ''' \n     
    
                    \t### Menu ###
    [1]\tDepositar 
    [2]\tSaque 
    [3]\tExtrato
    [4]\tNova conta
    [5]\tLista contas
    [6]\tNovo usuário
    [0]\tSair
=> '''
    return input(textwrap.dedent(menu))

# Def pra recupermos contas 
def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n###Cliente não possui conta! ###")
        return 
    
    # FIXME: não permitido escolher a conta!
    return cliente.contas[0]

# def depositar
def depositar(clientes):
    
    cpf = input("Informe seu CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n##\tCliente não encontrado!\t###")
        return

    valor = float(input("Informe o valor do deposito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

# def sacar
def sacar(clientes):
    cpf = input("Informe seu cpf: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente: 
        print("\n###Cliente não encontrado!### ")
        return
    
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

# exibindo extrato 
def exibir_extrato(clientes):
    cpf = input("Informe seu CPF: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("\n###Cliente não encontrado! ###")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("########## EXTRATO ##########")
    transacoes = conta.historico.transacoes 

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações! "

    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}: \n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("================================")

# criando usuário   
def criar_cliente(clientes):
    cpf = input("Informe o cpf (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if cliente:
        print("\n###já existe usuario com esse CPF! ###")
        return

    nome = input("Informe o nome complete: ")
    data_nascimento = input("Informe seu nascimento (DD/MM/AA):")
    endereço =  input("Informe o endereço (Logradouro, nro - Bairro - cidade/sigla estado): ")

    cliente = PessoaFisica( nome=nome,
                            data_nascimento=data_nascimento,
                            cpf=cpf, 
                            endereço=endereço )

    clientes.append(cliente)

    print("\n### Cliente criado com sucesso! ")


#def filtrar cliente
def filtrar_cliente(cpf, clientes):

    clientes_filtrados = [cliente for cliente in
    clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

# def criar conta
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do usuario: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n###\tCliente não encontrado, fluxo de criação de conta encerrado!\t###")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
        
    print("\n### Conta criada com sucesso! ###")

# def listar contas
def listar_contas(contas): 
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))



def main():

    clientes = []
    contas = []



    while True:
        opcao = menu()
        
        # opção deposito        
        if opcao == "1":
            depositar(clientes)
        
        # opção saque 
        elif opcao == "2":
            sacar(clientes)
        
        # opção extrato    
        elif opcao == "3":
            exibir_extrato(clientes)
        
        # opção de criar conta
        elif opcao == "4":
           numero_conta = len(contas) + 1
           criar_conta(numero_conta, clientes, contas)

        # opção de listar contas 
        elif opcao == "5":
            listar_contas(contas)

        # opção criar usuario
        elif opcao == "6":
            criar_cliente(clientes)
        
        # opção pra sair do programa  
        elif opcao == "0":
            break

        else:
            print("operação invalida, por favor selecione a operação desejada.")

main()
