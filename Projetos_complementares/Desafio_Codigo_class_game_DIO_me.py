'''
    Desafio de codigo DIO.me - class game
    Autor: Emerson Ricardo de Oliveira Silva
'''

# declarando class pra construção do programa
class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    # criando função pra cadastro de Heroi
    def cadastroPersonagem(nome, idade, tipo):
        
        print('*'*60)
        print('\t\t\tIniciando programa - Bem vindo!')
        
        print('*'*60)
        nome = input('Coloque o nome do seu personagem: ')
        idade = int(input('Coloque a idade do seu personagem: '))
        
        print('Classes do game: \n',
                '\t\t\t1 = Mago\n',
                '\t\t\t2 = Guerreiro\n',
                '\t\t\t3 = Monge\n',
                '\t\t\t4 = Ninja')
        
        print('*'*60)
        tipo = int(input('Numero do heroi escolhido: '))
        print('*'*60)

        # criando estrutura de decisão Mago, Guerreiro, Monge, Ninja
        if tipo == 1:
            print(f'{nome}, seu personagem escolhido é um Mago')
            print('Magos usam magia pra atacar e se defender!')
            print('Você ataca com um mago que sua magia!')
            print(f'Bom jogo {nome}!')

        elif tipo == 2:
            print(f'{nome}, seu personagem escolhido é um Guerreiro')
            print('Guerreiros usam espadas pra atacar e se defendem com escudos!')
            print('Você ataca com um guerreiro que sua espada!')
            print(f'Bom jogo {nome}!')

        elif tipo == 3:
            print(f'{nome}, seu personagem escolhido é um Monge')
            print('Monges artes marciais pra ataque e defesa!')
            print('Você ataca com um monge que sua artes marciais!')
            print(f'Bom jogo {nome}!')
        
        else:
            print(f'{nome}, seu personagem escolhido é um Ninja')
            print('Ninjas usam shuriken pra ataques e desefa!')
            print('Você ataca com um ninja que sua shuriken!')
            print(f'Bom jogo {nome}!')
              
        return nome, idade, tipo

                    
# criando saída de dados
def main():
    Heroi.cadastroPersonagem(nome=str, idade=int, tipo=int)
    
if __name__=='__main__':
    main()




