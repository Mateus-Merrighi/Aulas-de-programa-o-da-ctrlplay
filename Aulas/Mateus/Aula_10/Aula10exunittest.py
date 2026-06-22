import unittest

from Aula_10.Aula10exercícios import prova

class ProvaTest(unittest.TestCase):
    # def setUp(self):
    #     self.p= prova()
    #     self.r= 18090
    #     self.q= "Quanto é 90*201?"
    
    def test_armazenaQuestao(self):
        questao= "Quanto é 90*201?"
        p= prova()
        p.armarzena_questao_resposta(questao,"")
        self.assertIn("Quanto é 90*201?", p.questao)
    
    def test_armazenaResposta(self):
        resposta= "18090"
        p= prova()
        p.armarzena_questao_resposta("",resposta)
        self.assertIn("18090", p.resposta)
if __name__== '__main__':
    unittest.main(argv=[' '], exit=False)
        
