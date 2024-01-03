import threading
import Thread
import time


def car_1(velocidade, piloto):
    trajeto = 0

    while trajeto <= 100:

        trajeto += velocidade
        time.sleep(0.5)
        print("Piloto: {} KM: {}".format(piloto, trajeto))


# def car_2(velocidade):
#     trajeto = 0
#
#     while car_2 <= 100:
#         print("Carro_2: ", trajeto)
#         trajeto += velocidade



t_carro_1 = Thread(target=car_1, args=[1, 'Bruno'])
t_carro_2 = Thread(target=car_1, args=[1.5, 'teste'])

t_carro_1.start()
t_carro_2.start()
