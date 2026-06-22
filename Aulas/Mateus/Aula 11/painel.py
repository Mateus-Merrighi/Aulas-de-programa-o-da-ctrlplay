import suprimentos, math, os

agua= suprimentos.calcular_agua(14,5)
comida= suprimentos.calcular_comida(14,5)

print(f"Comida total: {comida} \n Agua total: {agua}")


aguareal= math.ceil(agua)
print(aguareal)

if os.path.exists("lixo_espacial.txt"):
    os.remove("lixo_espacial.txt")
    print("Ele sabia demais, precisava ter o cpf cancelado ")
else:
    print("Não há nenhuma suspeita perigosa no momento")