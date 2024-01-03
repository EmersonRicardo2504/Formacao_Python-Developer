import os # importar o modulo ou biblioteca OS 
            # (integra os porgramas com o sistema operacional  )

print("#" * 60) #imprimindo 60 vezes

ip_ou_host = input("Digite o IP ou Host a ser verificado: ")
# criamos um variavel que vai receber do usuario um ip

print("-" * 60)
os.system('ping -n 6 {}'.format(ip_ou_host)) #chamando system da biblioteca OS - comando ping

print("-" * 60) #imprimindo 60 vezes

