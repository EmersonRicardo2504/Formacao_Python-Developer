
# criando clases 
class animal:
    # função pra iniciar class
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
       


    def __str__(self):
        return f"{self.__class__.__name__}: {','.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}" 


class Mamifero(animal):
     # função pra iniciar class
    def __init__(self,cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        # self.nro_patas = nro_patas ## <--> consigo fazer a chama da classe dessa forma e com super()
        # dessa forma consigo chamar a função pai com super()
        super().__init__(**kw)



class Ave(animal):
     # função pra iniciar class
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

    
class Gato(Mamifero):
    pass 

class Cachorro(Mamifero):
    pass 

class Leao(Mamifero):
    pass 

class Orninorico(Mamifero, Ave):
    def __init__(self,cor_bico, nro_patas, cor_pelo):
        # print(Orninorico.__mro__)

        super().__init__(cor_bico=cor_bico, nro_patas=nro_patas, cor_pelo=cor_pelo)



gato = Gato(nro_patas=4, cor_pelo="Preta")
print(gato)

ornintorrico = Orninorico(nro_patas=2, cor_pelo="Branco", cor_bico="Laranja")
print(ornintorrico)
