tarefa= input("Tarefa desejada: ")
with open("taferas_seila3.txt", "a") as arquivo:
    arquivo.write(tarefa+"\n")
with open("taferas_seila3.txt", "r") as arquivo:
    linhas= arquivo.readlines()
    print("Quantidade de tarefas: ", len(linhas))
with open("taferas_seila3.txt", "r") as arquivo:
    for linha in arquivo:
       print(linha.strip())