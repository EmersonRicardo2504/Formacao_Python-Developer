proposta = """

- João tem uma bicicleta e gostaria de registrar as vendas de suas bicicletas 
- Crie um programa onde João informe: cor, modelo, ano, e valor da bicicleta vendida
- Uma bicicleta pode buzinar, parar e correr adicionar tais comportamentos 

"""
print(proposta)


# fazendo a classe 
class bicicleta:

    # fazendo as caracteristicas da bike  
    def __init__(self, modelo, cor, valor):
        self.modelo = modelo
        self.cor = cor
        self.valor = valor 

    def buzinar(self):
        print("plim plim")

    def parar(self):
        print("Freiando é rapída... ")
        print("Freio a disco. ")
        
    def correndo(self):
        print("Otíma para alcançar altas velocidades!  ")
        print("Cambio 6 marchas. ")

    def __str__(self):
        return f"{self.__class__.__name__} : {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# relizando impressão 
# para que ela seja realizada com sucesso devemos chama-la pelo print(nome.atributo) ou nome.atributo ()

# exemplo 1
print("\t\tExemplo 1")
b1 = bicicleta("Caloi", "Azul", 1000 )
print(b1.cor, b1.modelo, b1.valor)
b1.buzinar() 
b1.parar()
b1.correndo()


# exemplo 2
print("\n\t\tExemplo 2")
b2 = bicicleta("modelo_0", "cor_0", 0  )
print(b2)
# print(b2.modelo, b2.cor, b2.valor)
b2.buzinar()
b2.parar()
b2.correndo()


