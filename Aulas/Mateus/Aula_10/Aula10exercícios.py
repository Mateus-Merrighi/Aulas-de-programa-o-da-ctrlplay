class prova:
    def __init__(self):
        self.questao= []
        self.resposta= []
    def armarzena_questao_resposta(self, questao, resposta):
        if questao != "":
            self.questao.append(questao)
        if resposta!= "":
            self.resposta.append(resposta)
       
        
