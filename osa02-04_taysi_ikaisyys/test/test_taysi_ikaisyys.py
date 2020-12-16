import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.taysi_ikaisyys'

@points('2.taysi_ikaisyys')
class TaysiIkaisyysTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', retun_value ='0'):
            cls.module = load_module(exercise, 'fi')

    def test_taysi_ikaiset(self):
        values = "18 24 96 102".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                output = get_stdout().split("\n")
            
                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä syötteellä {}".format(len(output), value))
                self.assertEqual(output[0], f"Olet täysi-ikäinen!", f"Syötteellä {value} tulosteen pitäisi olla 'Olet täysi-ikäinen!', nyt se on " + output[0])

    def test_alaikaiset(self):
        values = "17 11 8 3".split(" ")
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                output = get_stdout().split("\n")
            
                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä syötteellä {}".format(len(output), value))
                self.assertEqual(output[0], "Et ole täysi-ikäinen!", f"Syötteellä {value} tulosteen pitäisi olla 'Et ole täysi-ikäinen!', nyt se on " + output[0])
                
                

    
                
                

    


                 
            
   
if __name__ == '__main__':
    unittest.main()
