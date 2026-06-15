import unittest
 
from Aula10 import nomenaordem

class NomesTest(unittest.TestCase):
    def test_nomenaordem(self):
        resultado=nomenaordem("João", "PVP", "Proplayer")
        self.assertEqual(resultado, "João PVP Proplayer")
if __name__== '__main__':
    unittest.main(argv=[' '], exit=False)