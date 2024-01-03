# importando biblioteca
from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.climatempo.com.br/").content


# objeto site recebendo o conteudo a pedido http do site
soup = BeautifulSoup(site, 'html.parser')

#   objeto soup baixando https do site
print(soup.prettify())

#   realizando uma chamada ordenada
temperatura = soup.find("span", class_=" _block _margin-b-5 -gray")
print(temperatura)
