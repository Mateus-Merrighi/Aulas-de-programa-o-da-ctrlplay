alcool= 0
gasosa=0
diesel=0
while True :
    print("---Preferencias dos clientes---")
    print("1- Álcool")
    print("2- Gasolina")
    print("3- Diessel")
    print("4-Fim")
    opcao=int(input('escolha uma das alternativas: '))
    if opcao== 1:
        alcool+= 1
    elif opcao== 2:
        gasosa+=1
    elif opcao == 3:
        diesel+=1
    elif opcao ==4:
        print(f"MUITO OBRIGADO\n Alcool:{alcool}\n Gasolina: {gasosa}\n Diesel: {diesel}")
        break
    

    
        
     
