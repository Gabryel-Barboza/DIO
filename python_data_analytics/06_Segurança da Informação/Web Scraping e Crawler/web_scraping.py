import requests
from bs4 import BeautifulSoup
# Web scraping refere-se a uma ferramenta para coletar dados de páginas da web


# Requisitando o corpo do site
site = requests.get("https://www.climatempo.com.br").content
# Criando um objeto do BeautifulSoup com a requisição
soup = BeautifulSoup(site, "html.parser")
# Imprimindo corpo HTML
#print(soup.prettify())
temperatura = soup.find("span", {"id": "current-weather-temperature"})
print(temperatura)
