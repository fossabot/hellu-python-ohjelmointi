import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.syotteen_rajaus'

def format_tuple(d : list):
    return str(tuple(d)).replace("'","")

@points('2.syotteen_rajaus')
class JatketaankoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect =["0"]):
            cls.module = load_module(exercise, 'fi')

    def test_1_lopetus(self):
        values = "1 0".split(" ")
    
        with patch('builtins.input', side_effect = values):
            try:
                reload_module(self.module)
                output = get_stdout()
            except:
                self.assertTrue(False, "Varmista, että ohjelma lopettaa toiminnan syötteellä {}".format(values))


    def test_2_lukuja_ja_lopetus(self):
        values = "9 4 16 1 0".split(" ")
        correct = "3.0\n2.0\n4.0\n1.0\nLopetetaan..."

        with patch('builtins.input', side_effect = values):
            reload_module(self.module)
            output = get_stdout()
            
            self.assertTrue(len(output.split("\n")) == 5, "Ohjelmasi tulostaa kyselyjen lisäksi viiden sijasta {} riviä\n{}\nkun syöte on {}".format(len(output.split("\n")), output, format_tuple(values)))
            self.assertTrue(output == correct, "Tulostus \n{} \nei vastaa oikeaa tulostetta \n{} \nkun syöte on {}".
                format(output, correct, format_tuple(values)))

    def test_3_epakelpo(self):
        values = "-1 0".split(" ")

        with patch('builtins.input', side_effect = values):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, "Varmista, että ohjelmasi toimii syötteellä {}".format(values))

    def test_4_lukuja_epakelpo_ja_lopetus(self):
        values = "9 4 16 -1 0".split(" ")
        correct = "3.0\n2.0\n4.0\nEpäkelpo luku\nLopetetaan..."

        with patch('builtins.input', side_effect = values):
            try:
                reload_module(self.module)
            except:
                self.assertTrue(False, "Varmista, että ohjelmasi toimii syötteellä {}".format(values))

            output = get_stdout()
            
            self.assertTrue(len(output.split("\n")) == 5, "Ohjelmasi tulostaa kyselyjen lisäksi viiden sijasta {} riviä:\n{}\nkun syöte on {}".format(len(output.split("\n")), output, format_tuple(values)))
            self.assertTrue(output == correct, "Tulostus \n{} \nei vastaa oikeaa tulostetta \n{} \nkun syöte on {}".
                format(output, correct, format_tuple(values)))

    def test_5_pelkka_lopetus(self):
        values = "0".split(" ")
        correct = "Lopetetaan..."

        with patch('builtins.input', side_effect = values):
            reload_module(self.module)
            output = get_stdout()
            
            self.assertTrue(len(output.split("\n")) == 1, "Ohjelmasi tulostaa kyselyjen lisäksi yhden sijasta {} riviä:\n{}\nkun syöte on {}".format(len(output.split("\n")), output, format_tuple(values)))
            self.assertTrue(output == correct, "Tulostus \n{} \nei vastaa oikeaa tulostetta \n{} \nkun syöte on {}".
                format(output, correct, format_tuple(values)))

if __name__ == '__main__':
    unittest.main()
