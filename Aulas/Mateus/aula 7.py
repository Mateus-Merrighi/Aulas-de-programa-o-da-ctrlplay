# primeiro pilar da poo abstração, pegar objetos, atributos e metodos que importam para o seu sistema
# class cachorro:
#     def __init__(self,nome,idade,raca):
#         self.nome= nome
#         self.__idade= idade
#         self.raca= raca
#     def latir(self):
#         print(f'{self.nome} está latindo')
#     def get_idae(self):
#         return print(f"{self.__idade}, ele é sábio")
#     def set_idade(self,nova_idade):
#         if nova_idade >= 0 :
#             self.__idade= nova_idade
#         else:
#             print("Idade Inválida, precisar ser maior ou igual a 0")
 
# Chihuahua= cachorro("kleber", 5, "Chihuahua")
# Chihuahua.latir()
# print(Chihuahua.get_idae())
# Chihuahua.set_idade(1000)
# print(Chihuahua.get_idae())
# class animal:
#     def __init__(self,nome, idade):
#        self.nome=nome
#        self.idade= idade
#     def comer(self):
#         print(f"{self.nome} está comendo")
#     def respira(self):
#         print(f"{self.nome} está respirando")
# class Cachorro(animal):
#     def latir(self):
#         print(f"{self.nome}está latindo, au aua uaauaau uauauauau a u")
# class Cobra(animal):
#     def rastejar(self):
#         print(f"{self.nome}está rastejando.")
# Sebastian= Cachorro("Thor", 1000,)
# Cleitin=Cobra("Cleitin PvP", 10000000000000000000000000000000009)
# Sebastian.respira()
# Sebastian.comer()
# Sebastian.latir()
# Cleitin.respira()
# Cleitin.comer()
# Cleitin.rastejar()
class Aves:
    def voa(self):
        print(" A ave está voando")
class Pinguim(Aves):
    def voa(self):
        print('O piguim não consegue voar')
Kleiton= Pinguim()
Kleiton.voa()
