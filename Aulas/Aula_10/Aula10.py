
def nomenaordem(nome, sobrenome1, sobrenome2):
    if len(sobrenome1)> len(sobrenome2):
        return nome+' '+sobrenome1 + ' '+sobrenome2
    else:
        return nome+' '+ sobrenome2+' '+sobrenome1
print(nomenaordem("Mateus", "play", "games"))