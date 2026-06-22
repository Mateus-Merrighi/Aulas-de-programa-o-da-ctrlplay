import requests as r
from bs4 import BeautifulSoup
try:
    resultado=r .get("https://poki.com/br/g/dragon-simulator-3d")
except Exception as erro:
    print("Erro: ", erro)
else:
    resposta= resultado.text
    soup= BeautifulSoup(resposta, "html.parser")
    # print(soup.find("h1"))
    print(soup.find("h1", class_="TIakIJk_seZmjAw2Dhmw").prettify())
