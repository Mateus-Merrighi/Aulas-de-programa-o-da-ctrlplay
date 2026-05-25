# r= read- lendo oque esta nele
# w= write- apaga tudo e escreve por cima
# a= append- adiciona o arquivo
# r+ = ler e escrever
# with open("sei lá.txt","r") as arquivo:
#     print(arquivo.read()
with open("fruta_seila2.txt","r") as arquivo:
    print(arquivo.read())
fruta = input("Digite o nome de uma fruta: ")
with open("fruta_seila2.txt","a") as arquivo:
    arquivo.write(fruta + "\n")
    print("Fruta adiciona com sucesso! ")
with open("fruta_seila2.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    print("Quantidade de linhas:", len(linhas))

with open("fruta_seila2.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())
