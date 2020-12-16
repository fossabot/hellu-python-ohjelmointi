import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.korjaa_virheet'

@points('2.korjaa_virheet')
class KorjaaVirheetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', retun_value ='0'):
            cls.module = load_module(exercise, 'fi')

    def test_yli_sata_0(self):
        value = 101
        with patch('builtins.input', return_value = str(value)):
            try:
                reload_module(self.module)
                output = get_stdout().split("\n")
            except:
                self.assertTrue(False, "varmista että pystyt suorittamaan ohjelman syötteellä {}".format(value))


    def test_alle_sata_0(self):
        value = 90
        with patch('builtins.input', return_value = str(value)):
            try:
                reload_module(self.module)
                output = get_stdout().split("\n")
            except:
                self.assertTrue(False, "varmista että pystyt suorittamaan ohjelman syötteellä {}".format(value))

    def test_alle_sata_1(self):
        value = randint(1,99)
        with patch('builtins.input', return_value = str(value)):
            reload_module(self.module)
            output = get_stdout().split("\n")
        
            self.assertTrue(len(output) == 2, "Ohjelmasi tulostaa kahden rivin sijasta {} riviä syötteellä {}".format(len(output), value))
            self.assertTrue(output[0].find(str(value)) > -1, "Tulosteesta ei löydy oikeaa lukua {} syötteellä {}".format(value, value))
            self.assertEqual(output[0], str(value) + " taitaa olla onnenlukuni!", "Tulosteen 1. rivi ei vastaa mallivastausta syötteellä {}".format(value))
            self.assertEqual(output[1], "Hyvää päivänjatkoa!", "Tulosteen 2. rivi ei vastaa mallivastausta syötteellä {}".format(value))
            
    def test_alle_sata_2(self):
        value = randint(1,99)
        with patch('builtins.input', return_value = str(value)):
            reload_module(self.module)
            output = get_stdout().split("\n")
        
            self.assertTrue(len(output) == 2, "Ohjelmasi tulostaa kahden rivin sijasta {} riviä syötteellä {}".format(len(output), value))
            self.assertTrue(output[0].find(str(value)) > -1, "Tulosteesta ei löydy oikeaa lukua {} syötteellä {}".format(value, value))
            self.assertEqual(output[0], str(value) + " taitaa olla onnenlukuni!", "Tulosteen 1. rivi ei vastaa mallivastausta syötteellä {}".format(value))
            self.assertEqual(output[1], "Hyvää päivänjatkoa!", "Tulosteen 2. rivi ei vastaa mallivastausta syötteellä {}".format(value))

    def test_yli_sata_1(self):
        value = randint(100,10000)
        with patch('builtins.input', return_value = str(value)):
            reload_module(self.module)
            output = get_stdout().split("\n")
        
            self.assertTrue(len(output) == 5, "Ohjelmasi tulostaa viiden rivin sijasta {} riviä syötteellä {}".format(len(output), value))
            self.assertTrue(output[2].find(str(value - 100)) > -1, "Tulosteesta ei löydy pienennettyä lukua {} syötteellä {}".format(value - 100, value))
            self.assertEqual(output[0], "Luku oli suurempi kuin sata", "Tulosteen 1. rivi ei vastaa mallivastausta syötteellä {}".format(value))
            self.assertEqual(output[1], "Nyt luvun arvo on pienentynyt sadalla", "Tulosteen 2. rivi ei vastaa mallivastausta syötteellä {}".format(value))
            self.assertEqual(output[3], str(value - 100) + " taitaa olla onnenlukuni!", "Tulosteen 4. rivi ei vastaa mallivastausta syötteellä {}.format(value)")
            self.assertEqual(output[4], "Hyvää päivänjatkoa!", "Tulosteen 5. rivi ei vastaa mallivastausta")

    def test_yli_sata_2(self):
        value = randint(100,10000)
        with patch('builtins.input', return_value = str(value)):
            reload_module(self.module)
            output = get_stdout().split("\n")
        
            self.assertTrue(len(output) == 5, "Ohjelmasi tulostaa viiden rivin sijasta {} riviä syötteellä {}".format(len(output), value))
            self.assertTrue(output[2].find(str(value - 100)) > -1, "Tulosteesta ei löydy pienennettyä lukua {} syötteellä {}".format(value - 100, value))
            self.assertEqual(output[0], "Luku oli suurempi kuin sata", "Tulosteen 1. rivi ei vastaa mallivastausta. syötteellä {}".format(value))
            self.assertEqual(output[1], "Nyt luvun arvo on pienentynyt sadalla", "Tulosteen 2. rivi ei vastaa mallivastausta. syötteellä {}".format(value))
            self.assertEqual(output[3], str(value - 100) + " taitaa olla onnenlukuni!", "Tulosteen 4. rivi ei vastaa mallivastausta ".format(value))
            self.assertEqual(output[4], "Hyvää päivänjatkoa!", "Tulosteen 5. rivi ei vastaa mallivastausta".format(value))
    
if __name__ == '__main__':
    unittest.main()
