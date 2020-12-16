import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.lampotilat'

@points('1.lampotilat')
class LampotilatTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_nolla(self):
        test_input = 32
        correct = (test_input - 32) * 5/9
        with patch('builtins.input', return_value = str(test_input)):
            reload_module(self.module)
            output = get_stdout().lower().split("\n")
            self.assertEqual(len(output), 1, "Ohjelmasi tulosti useamman kuin yhden rivin")
            self.assertTrue(output[0].find("0.0") > -1, "Ohjelma ei muuntanut lämpötilaa oikein: lopputuloksen pitäisi olla 0.0, mutta ohjelmasi tulostaa " + output[0])
            self.assertFalse(output[-1].find("paleltaa") > -1, "Ohjelmasi tulosti viestin 'Paleltaa!' vaikka lämpötila celsiuksina ei ole alle nollan.")
            #corr_str = "{} fahrenheit-astetta on {} celsius-astetta".format(test_input, correct)
            #self.assertEqual(output[0], corr_str, "Tulostus ei ollut oikein: piti olla {}, mutta ohjelmasi tulosti {}".format(corr_str, output[0]))
            
    def test_positiivinen(self):
        test_input = randint(33, 105)
        correct = (test_input - 32) * 5/9
        with patch('builtins.input', return_value = str(test_input)):
            reload_module(self.module)
            output = get_stdout().lower().split("\n")
            self.assertEqual(len(output), 1, "Ohjelmasi tulosti useamman kuin yhden rivin")
            self.assertTrue(output[0].find(str(correct)[:3]) > -1, "Ohjelma ei muuntanut lämpötilaa oikein: lopputulokset syötteellä {} pitäisi olla {}, mutta ohjelmasi tulostaa {}".format(test_input, correct, output[0]))
            self.assertFalse(output[-1].find("paleltaa") > -1, "Ohjelmasi tulosti viestin 'Paleltaa!' vaikka lämpötila celsiuksina ei ole alle nollan.")
            #corr_str = "{} fahrenheit-astetta on {} celsius-astetta".format(test_input, correct)
            #self.assertEqual(output[0], corr_str, "Tulostus ei ollut oikein: piti olla {}, mutta ohjelmasi tulosti {}".format(corr_str, output[0]))

    def test_negatiivinen(self):
        test_input = randint(-50, 31)
        correct = (test_input - 32) * 5/9
        with patch('builtins.input', return_value = str(test_input)):
            reload_module(self.module)
            output = get_stdout().lower().split("\n")
            self.assertTrue(output[0].find(str(correct)[:3]) > -1, "Ohjelma ei muuntanut lämpötilaa oikein: lopputulokset syötteellä {} pitäisi olla {}, mutta ohjelmasi tulostaa {}".format(test_input, correct, output[0]))
            self.assertTrue(output[1].find("paleltaa") > -1, "Ohjelmasi ei tulostanut viestiä 'Paleltaa!' vaikka lämpötila celsiuksina on alle nollan.")
            #corr_str = "{} fahrenheit-astetta on {} celsius-astetta".format(test_input, correct)
            #self.assertEqual(output[0], corr_str, "Tulostus ei ollut oikein: piti olla {}, mutta ohjelmasi tulosti {}".format(corr_str, output[0]))



                 
            
   
if __name__ == '__main__':
    unittest.main()
