import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.nimi_ja_osoite'

@points('1.nimi_ja_osoite')
class NimiJaOsoiteTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = ''):
            cls.module = load_module(exercise, 'fi')

    def test_tulostus_1(self):
        test_input = "Pekka,Python,Pythonpolku 1,12345 Pythonila"
        test_output = "Pekka Python,Pythonpolku 1,12345 Pythonila".split(",")
        with patch('builtins.input', side_effect = test_input.split(",")):
            reload_module(self.module)
            output = get_stdout().split("\n")
            self.assertTrue(len(output) == 3, "Ohjelmasi ei tulostanut 3 riviä vaan " + str(len(output)))            
            for i in range(3):
                self.assertEqual(output[i], test_output[i], '{}. rivi ei tulostunut oikein oikein syötteillä {}'.format((i + 1), test_input))
    
    def test_tulostus_2(self):
        test_input = "Keijo,Keksitty,Keksikuja 123 A 1,98765,Keksilä"
        test_output = "Keijo Keksitty,Keksikuja 123 A 1,98765,Keksilä".split(",")
        with patch('builtins.input', side_effect = test_input.split(",")):
            reload_module(self.module)
            output = get_stdout().split("\n")
            self.assertTrue(len(output) == 3, "Ohjelmasi ei tulostanut 3 riviä vaan " + str(len(output)))            
            for i in range(3):
                self.assertEqual(output[i], test_output[i], '{}. rivi ei tulostunut oikein oikein syötteillä {}'.format((i + 1), test_input))

    def test_tulostus_3(self):
        test_input = "Maija Marjukka,Mielikuvitushahmo,Mielikuja 555 as. 234,12121,Tampere"
        test_output = "Maija Marjukka Mielikuvitushahmo,Mielikuja 555 as. 234,12121,Tampere".split(",")
        with patch('builtins.input', side_effect = test_input.split(",")):
            reload_module(self.module)
            output = get_stdout().split("\n")
            self.assertTrue(len(output) == 3, "Ohjelmasi ei tulostanut 3 riviä vaan " + str(len(output)))            
            for i in range(3):
                self.assertEqual(output[i], test_output[i], '{}. rivi ei tulostunut oikein oikein syötteillä {}'.format((i + 1), test_input))
            
   
    #def test_syotetta_kysytaan_tasmalleen_kerran(self):
    #    with patch('builtins.input', return_value = '') as prompt:
     #       reload_module(self.module)
     ##       output = get_stdout()
      ##      try:
        #        prompt.assert_called_once()
         #   except AssertionError:
          #      self.fail('Syötettä tulee pyytää täsmälleen kerran.')

if __name__ == '__main__':
    unittest.main()
