def book():
    dicionario= {"cat": "gato", "dog": "cahorro","bank":"banco", "park":"parque","car":"carro"}
    select = input("Digite uma palvra em inglês: ").lower()
    if select in dicionario:
        print("Tradução: ", dicionario[select])
    else:
        print("Palavra não encontrada")
    for chave in dicionario:
        print(chave)
book()
