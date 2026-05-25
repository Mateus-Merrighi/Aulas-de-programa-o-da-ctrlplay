class livro:
    def __init__(self, titulo, autor, qutd_paginas):
        self.titulo= titulo
        self.autor= autor
        self.qutd_paginas= qutd_paginas
        self.emprestado= False
        
    def informaçõesDoLivro(self):
        print("Título: ",self.titulo)
        print("Autor: ",self.autor)
        print(self.qutd_paginas)
        print("Emprestado", self.emprestado)
    def emprestar(self):
        if self.emprestado is False:
            print(f"Você adiquiriu o livro {self.titulo} com sucesso ")
            self.emprestado=True
        else:
            print(f"O livro {self.titulo} não esta disponível")
    def devolver(self):
        if self.emprestado is True:
            self.emprestado = False
            print(f"Você devolveu o livro {self.titulo} com sucesso ")
        else:
            print(f"O livro {self.titulo} já esta disponível")
livro1= livro("e","aim",200)
livro1.informaçõesDoLivro()
livro1.emprestar()
livro1.informaçõesDoLivro()
livro1.emprestar()
livro1.devolver()
livro1.emprestar()
      
            

     

    