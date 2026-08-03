# class casa:
#     rua= "Rua Bernado Guimarães"
#     bairro= "Santo Agostinho" 
#     cep= "12345-678" 
#     def enderecoCompleto(self):
#       print(casa.rua)
#       print(casa.bairro)
#       print(casa.cep)
# # obs: print(type(something))
# ctrlplay= casa()
# ctrlplay.enderecoCompleto()
class casa:
   Cidade = "BH" #atributo da classe
   def __init__(self, rua, bairro, cep):
      self.rua= rua #atributos do objeto
      self.bairro= bairro #atributos do objeto
      self.cep=cep #atributos do objeto
   def endereçoCompleto(self):
         print(casa.Cidade)
         print(self.rua)
         print(self.bairro)
         print(self.cep)

casaMerrighi= casa("Rua Tomé de Souza 10", "Savassi", "11112-223")
casaMerrighi.endereçoCompleto()