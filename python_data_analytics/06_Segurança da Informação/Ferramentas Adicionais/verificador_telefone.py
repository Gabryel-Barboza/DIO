import phonenumbers
from phonenumbers import geocoder

# Criando um verificador de localidade de telefone

telefone = input("Digite o telefone no formato: (+551199999999): ")
# Convertendo para um objeto phonenumber
numero_telefone = phonenumbers.parse(telefone)

# Verifica a localização do telefone inserido
print(geocoder.description_for_number(numero_telefone, "pt"))
