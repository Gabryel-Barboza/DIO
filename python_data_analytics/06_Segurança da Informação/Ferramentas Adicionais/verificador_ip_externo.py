import json
import re
from urllib.request import urlopen

# Verifica o ip externo da máquina
url = "https://ipinfo.io/json"
response = urlopen(url)
dados = json.load(response)

print(dados["ip"], dados["city"])
