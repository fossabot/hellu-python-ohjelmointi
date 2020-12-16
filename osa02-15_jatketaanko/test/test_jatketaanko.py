import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.jatketaanko'

def format_tuple(d : tuple):
    return str(d).replace("'","")

@points('2.jatketaanko')
class JatketaankoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =["ei"]):
            cls.module = load_module(exercise, 'fi')

    def test_ensimmainen(self):
        values = "jatka ei".split(" ")
    
        with patch('builtins.input', side_effect = values):
            try:
                reload_module(self.module)
                output = get_stdout()
            except:
                self.assertTrue(False, "Varmista, että ohjelma pysähtyy syötteellä {}".format(values))

    def test_kolme_ja_ei(self):
        values = "jatka joo kyllä ei".split(" ")
    
        with patch('builtins.input', side_effect = values):
            reload_module(self.module)
            output = get_stdout()
            correct = "moi\nmoi\nmoi\nmoi\nei sitten"
            
            self.assertTrue(len(output.split("\n")) == 5, "Ohjelmasi tulostaa kyselyjen lisäksi viiden sijasta {} riviä: \n{}\nsyötteellä {}".format(len(output.split("\n")), output, format_tuple(values)))
            self.assertTrue(output == correct, "Tulostus {} ei vastaa oikeaa tulostetta {} kun syöte on {}".
                format(output[0], correct, tuple(values)))

    def test_yksi_ja_ei(self):
        values = "mitä ei".split(" ")
    
        with patch('builtins.input', side_effect = values):
            reload_module(self.module)
            output = get_stdout()
            correct = "moi\nmoi\nei sitten"
            
            self.assertTrue(len(output.split("\n")) == 3, "Ohjelmasi tulostaa kolmen rivin sijasta {} riviä: \n{}\nkun syöte on {}".format(len(output.split("\n")), output, tuple(values)))
            self.assertTrue(output == correct, "Tulostus {} ei vastaa oikeaa tulostetta {} kun syöte on {}".
                format(output[0], correct, tuple(values)))

    def test_heti_ei(self):
        values = ["ei"]
    
        with patch('builtins.input', side_effect = values):
            reload_module(self.module)
            output = get_stdout()
            correct = "moi\nei sitten"
            
            self.assertTrue(len(output.split("\n")) == 2, "Ohjelmasi tulostaa kahden rivin sijasta {} riviä: \n{}\nkun syöte on {}".format(len(output.split("\n")), output, tuple(values)))
            self.assertTrue(output == correct, "Tulostus {} ei vastaa oikeaa tulostetta {} kun syöte on {}".
                format(output[0], correct, tuple(values)))
    
if __name__ == '__main__':
    unittest.main()
