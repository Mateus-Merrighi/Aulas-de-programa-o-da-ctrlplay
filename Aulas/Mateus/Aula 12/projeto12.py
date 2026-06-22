import requests as r
from bs4 import BeautifulSoup

url= "https://www.bbc.com/"
page= r.get(url)

soup= BeautifulSoup(page.content, "html.parser")

lista={'lol', 'valorant', 'fifa', 'fortnite'}

for paragrafo in soup.find_all('body'):
    for palavra in lista:
        for paragrafo_str in paragrafo.stripped_strings:
            if palavra.upper() in str(paragrafo_str).upper():
                print("NOTÍCIA SOBRE:", palavra.upper(), '\n', paragrafo_str, '\n')
                break