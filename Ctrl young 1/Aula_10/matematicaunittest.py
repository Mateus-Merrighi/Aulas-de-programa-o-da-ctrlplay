import unittest
from Aula_10.matematica import Calculadora
class matematicaTest(unittest.TestCase):
    def setUp(self):
        self.c= Calculadora
        self.a= 4
        self.b= 2
    def test_somandonumeros(self):
        self.assertEqual(self.c.somandonumeros(self.b,self.a), 6)
    def test_subtraindonumeros(self):
        self.assertEqual(self.c.subtraindonumeros(self.a,self.b), 2)
if __name__== '__main__':
    unittest.main(argv=[' '], exit=False)
               




    