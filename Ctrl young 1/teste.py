#1004
#raio= float(input())
# area=3.14159*(raio**2)
# print(f"A={area:.4f}")
# nome, salario fixo+ total da venda(15%)
# 1009
# Nome=input()
# salário=float(input())
# Bonus= float(input())
# total=salário+Bonus*0.15
# print(f"TOTAL = R$ {total:.2f}")
#litros, faz 12Km/L,  Tempo(h) Vmedia(km/h) a partir da distancia = litros gastos
#em deimal 3 casas, doi int t v
# 1017
# t= int(input())
# kmph=int(input())
# litros= (t*kmph)/12
# print(f"{litros:.3f}")
#1045
#A,B,C A>b,c
A=float(input()) 
B=float(input()) 
C=float(input())
if A<B:
    A,B=B,A
if A<C:
    A,C=C,A
if B<C:
    B,C=C,B
if A >= B+C:
    print("NÃO FORMA TRIANGULO") 
else:
 if A*2==B*2+C*2:
     print("TRIANGULO RETANGULO")
 elif A*2>B*2+C*2:
    print("TRIANGULO OBTUSANGULO")
 elif A*2<B*2+C*2:
    print("TRIANGULO ACUTANGULO")        
 if A==C and A==B:
      print("TRIANGULO EQUILATERO")
 elif A==C and A != B or A==B and A!=C or B==C and B!=A:
      print("TRIANGULO ISÓCELES")
    
    
    

