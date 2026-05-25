def calcular_media(notas):
    return sum(notas)/len(notas)
def verificar_situacao(media):
    if media>= 7:
        return "Aprovado"
    elif media>= 5:
        return "Recuperação"
    else:
        return "Reprovado"
def mostrat_boletim(nome,notas):
    media= calcular_media(notas)
    situacao= verificar_situacao(media)
    print(f"Aluno {nome}")
    print(f"Média {media}")
    print(f"Situação {situacao}")
mostrat_boletim("Zaarias",[10,9,10])