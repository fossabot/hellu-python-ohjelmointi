import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.fizzbuzz'

def format_tuple(d : tuple):
    return str(d).replace("'","")

def get_grade(p : int) -> str:
    if p == 100:
        return "5"
    return str((p - 50) // 10 + 1)

@points('2.fizzbuzz')
class FizzBuzzTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_fizz(self):
        values = "3 6 21 27 33 39 333".split(" ")
        correct = "Fizz"
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                output = get_stdout().split("\n")

                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä: {} kun syöte on {}".format(len(output), output, value))
                self.assertEqual(output[0].lower().strip(), correct.lower(), "Tulostus {} ei vastaa oikeaa tulostetta {} kun syöte on {}".
                    format(output[0], correct, value))

    def test_buzz(self):
        values = "5 20 35 65 550".split(" ")
        correct = "Buzz"
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                output = get_stdout().split("\n")

                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä: {} kun syöte on {}".format(len(output), output, value))
                self.assertEqual(output[0].lower().strip(), correct.lower(), "Tulostus {} ei vastaa oikeaa tulostetta {} kun syöte on {}".
                    format(output[0], correct, value))
    
    def test_fizzbuzz(self):
        values = "15 30 150 330 660".split(" ")
        correct = "FizzBuzz"
        for value in values:
            with patch('builtins.input', return_value = value):
                reload_module(self.module)
                output = get_stdout().split("\n")

                self.assertTrue(len(output) == 1, "Ohjelmasi tulostaa yhden rivin sijasta {} riviä: {} kun syöte on {}".format(len(output), output, value))
                self.assertEqual(output[0].lower().strip(), correct.lower(), "Tulostus {} ei vastaa oikeaa tulostetta {} kun syöte on {}".
                    format(output[0], correct, value))

   
                
                

    
if __name__ == '__main__':
    unittest.main()
