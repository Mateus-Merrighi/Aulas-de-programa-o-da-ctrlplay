def cadastro():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))
    print("Cadastro realisado")
    print("Nome:", nome)
    print("Idade:",idade)
    print("Altura:", altura)
    if idade < 0:
        print("Idade inválida")
    elif idade < 18:
        print("Menor de idade")
    else:
        print("Maior de Idade")
    if altura < 0 or altura >= 3.0:
        print("Altura inválida")
    elif altura < 1.20:
        print(f"{nome} não pode entrar no brinquedo")
    else:
        print(f"{nome} acesso liberado")
    

