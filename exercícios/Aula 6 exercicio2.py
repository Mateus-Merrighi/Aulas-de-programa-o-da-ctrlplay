class aluno:
    def __init__(self,nome,nota1,nota2,faltas):
      self.nome=nome
      self.nota1=nota1
      self.nota2=nota2
      self.faltas=faltas
    def calcular_media(self):
       return(self.nota1 + self.nota2)/2
    def situação(self):
       media= self.calcular_media
       if media< 7 or self.faltas>= 5:
          print(f"Infelizmento você, {self.nome}, foi reprovado")
       else:
          print(f"Parabéns {self.nome}, você passou de ano")
aluno1= aluno("Mateus", 10, 9, 2)
aluno3= aluno("Mateus", 1, 2, 2)
aluno2= aluno("Mateus", 10, 9, 5)

aluno2.calcular_media()
       
    