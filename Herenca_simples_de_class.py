
#  defindo a classe principal e seus atributos 

class veiculo(): 
    def __init__(self, cor, modelo, placa):
        self.cor = cor 
        self.modelo = modelo
        self.placa = placa

    def __str__(self):
        return f"{self.__class__.__name__}: {','.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}" 


    def ligar_motor(self):
        print("Motor ligado") 

    
    def desligar_motor(self):
        print("Desligando o motor")

    
# classes filhas sendo definidas -> motocicletas, carro, caminhão
class Motocicleta(veiculo):
    def teste_usabilidade(self):
        print("Atingiu velocidade máxima!")

class Carro(veiculo):
    def teste_usabilidade(self):
        print("Seguro!")

class Caminhao(veiculo):
    def __init__(self, cor, modelo, placa, carregado):
        super().__init__(cor,modelo,placa)
        self.carregado = carregado
            
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'}, aguentou carga máxima!")


# criando impressão de operações
moto = Motocicleta("Azul", "XT-660", "abc-1234" ) # moto("Azul", "XT-660", "abc-1234" )
carro = Carro("Cinza", "Fox", "LXN-5353")
caminhao = Caminhao("Preto", "Teste", 0, True)

# atenção !! Dessa forma somente veremos se a operação foi instanciada 
# podemos chamar as operações dessa forma também após receber os parametros
print(moto)
print(carro)
print(caminhao)

# dessa forma seria feita a chamada pra impressão

# print("\nMoto", moto.cor, moto.modelo, moto.placa)
# moto.ligar_motor()
# moto.teste_usabilidade()
# moto.desligar_motor()

# print("\nCarro", carro.cor, carro.modelo, carro.placa)
# carro.ligar_motor()
# carro.teste_usabilidade()
# carro.desligar_motor()

# print(caminhao.cor, caminhao.modelo, caminhao.placa)
# caminhao.ligar_motor()
# caminhao.esta_carregado()
# caminhao.desligar_motor()   