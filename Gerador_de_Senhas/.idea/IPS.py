import ipaddress


ip = '192.168.0.1'

endereco = ipaddress.ip_address(ip)
print(endereco)

print(endereco + 25000)

print("-"*60)

rede_1 = '198.168.0.1/1'
rede = ipaddress.ip_network(rede_1, strict=False)

for ip in rede:
    print(ip)
