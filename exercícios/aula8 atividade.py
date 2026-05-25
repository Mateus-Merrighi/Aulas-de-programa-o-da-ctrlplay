def banco():
    saldo= 1000
    while True:
        print("---Caixa Eletronico---")
        print("1- Ver saldo")
        print("2- Depositar")
        print("3- Sacar")
        print("4- Sair")
        try:
         
         opção= int(input("Escolha sua opção: "))
         if opção == 1:
            print(saldo)
         elif opção == 2:
            numero_de_deposito=float(input("Quanto vai ser depositado: "))
            if numero_de_deposito< 0:
                print("Valor inválido")
            else:
                saldo+=numero_de_deposito
                print(saldo)
         elif opção ==3:
            numero_de_saque= float(input("Quanto vai ser sacado: "))
            if numero_de_saque< 0 or numero_de_saque > saldo:
                print ( "Saque inválido: ")
            else:
                saldo-= numero_de_saque
                print(saldo)
         elif opção ==4:
            break
         else:
            print("Digite uma opção valida")
         
        
        except:
           print("Essa opção não existe, tente digitar números que correspondem com o seu saldo atual")
        finally:
           print("Reniciando sistema, se tiver finalizado clique sair")

banco()