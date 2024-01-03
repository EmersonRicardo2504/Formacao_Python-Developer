import random, string  # importando bibliotecas


tamanho = int(input("Coloque o tamnaho da sua senha: "))        # definindo tamanho da senha

#      passando caracteres que serão permitidos
chars = string.ascii_letters + string.digits + '!@#$%¨&*()ç_+={}`^'

rnd  = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))

