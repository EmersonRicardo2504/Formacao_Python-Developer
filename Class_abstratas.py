from abc import ABC

# criando a class 
class ControleRemoto(ABC):
    
    @classmethod
    def ligar(self):
        pass
    
    @classmethod
    def desligar(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando TV...")
        print("TV ligada !!")

    def desligar(self):
        print("Desligando TV")
        print("TV desligada!\n")

    @property
    def marca(self):
        return "Philco"

class Arcondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando ar...")
        print("Ar ligado!")

    def desligar(self):
        print("Desligando ar...")
        print("Ar desligado...")

    @property
    def marca(self):
        return "LG"


# impressão de dados 
print("\t\nexemplo 1")
controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

print("\t\nexemplo 2")
controle = Arcondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)
