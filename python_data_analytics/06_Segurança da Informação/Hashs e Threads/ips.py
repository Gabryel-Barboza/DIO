import ipaddress
# Realizando cálculos e interações com endereços IPs

ip = "192.168.0.1"
# Retorna um objeto de endereço ip
endereco = ipaddress.ip_address(ip)
# Realiza o cálculo de IP correto, mudando o endereço da rede quando ultrapassa o limite de hosts
print(endereco + 256)

ip_mascara = "192.168.0.100/24"
# Retorna um objeto de rede ip, strict para aceitar IP de host e detectar o endereço da rede automaticamente
rede = ipaddress.ip_network(ip_mascara, strict=False)
print(rede)

# Imprime todos os IPs para a rede especificada
for ip in rede:
    print(f"{ip} ")
