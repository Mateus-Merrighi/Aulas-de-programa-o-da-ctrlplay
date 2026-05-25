class pokedex:
    def __init__(self,nome, type, hp, nivel ):
        self.nome=nome
        self.type=type
        self.__nivel=nivel
        self.hp=hp

    def get_nivel(self):
        return print(f"Os status de {self.nome} são {self.hp}, {self.type} e {self.__nivel} ")
    
    def set_novo_nivel(self, novo_nivel):
        if novo_nivel > self.__nivel:
            self.__nivel= novo_nivel
        else:
            print("não é possível")

class iniciais:
    def incial(self):
        print(" Você possuí um inicial")
        
class aves(pokedex):
    def voador(self):
        print(F"{self.nome}, pode aprender fly")

class dudu(aves):
    def voador(self):
        print(F"{self.nome}, não pode aprender fly")

class charizard(pokedex,iniciais):
    def foda(self):
        print(" Este pokemon é foda")

Dudu=dudu("Aveztrus",", Voador", ", 1068hp", 100)
Dudu.get_nivel()
Dudu.set_novo_nivel(99)
Dudu.get_nivel()
Pigeot=aves("Passarinho,"," Voador,"," 20hp e ", 5)
Pigeot.get_nivel()
Pigeot.set_novo_nivel(20)
Pigeot.get_nivel()
Charizard= charizard("Dragão, ","Fogo e Voador, ","500hp", 50)
Charizard.get_nivel()
Charizard.incial()
Charizard.foda()
    
        