import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.lahjaverolaskuri'

@points('2.lahjaverolaskuri')
class LahjaverolaskuriTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_arvot(self):
        values = ["11400 612", "42450 3445", "195000 21500", "567800 77270", "10100200 1689134"]
        for valuegroup in values:
            testvalue, correct = valuegroup.split(" ")
            with patch('builtins.input', return_value = testvalue):
                reload_module(self.module)
                output = get_stdout().split("\n")

                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä: {} kun syöte on {}".format(len(output), output, testvalue))
                self.assertTrue(output[0].lower().strip().find("vero: " + correct) > -1, "Tulostus {} ei sisällä oikeaa tulosta {} kun syöte on {}".
                    format(output[0], correct, testvalue))

    def test_ei_veroa(self):
        values = [str(randint(0, 4999)) for i in range(5)]
        for testvalue in values:
            correct = "Ei veroa"
            with patch('builtins.input', return_value = testvalue):
                reload_module(self.module)
                output = get_stdout().split("\n")

                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä: {} kun syöte on {}".format(len(output), output, testvalue))
                self.assertTrue(output[0].lower().strip().find(correct.lower()) > -1, "Tulostus {} ei sisällä oikeaa tulosta {} kun syöte on {}".
                    format(output[0], correct, testvalue))



  
    
if __name__ == '__main__':
    unittest.main()
