import unittest
unittest.TestLoader.sortTestMethodsUsing = None
import importlib

from tmc import points

from tmc.utils import get_stdout, load_module, reload_module

exercise = 'src.ukko_nooa'
@points('1.ukko_nooa')
class UkkoNooaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(exercise, 'fi')

    def test_print_length(self):
        reload_module(self.module)
        split_output = get_stdout().split('\n')
        self.assertEqual(len(split_output), 3, 'Tulostuksessa väärä määrä rivejä.')

    def test_content(self):
        reload_module(self.module)
        split_output = get_stdout().split('\n')
        self.failIf(len(split_output) != 3, 'Tulostuksessa odotettiin olevan {0} riviä, ohjelmasi tulostaa tällä hetkellä {1} riviä.'.format(3, len(split_output)))
        self.assertEqual(split_output[0], 'Ukko Nooa, Ukko Nooa oli kunnon mies.', 'Ensimmäinen rivin tulostus väärin.')
        self.assertEqual(split_output[1], 'Kun hän meni saunaan, laittoi laukun naulaan.', 'Toisen rivin tulostus väärin.')
        self.assertEqual(split_output[2], 'Ukko Nooa, Ukko Nooa oli kunnon mies.', 'Kolmannen rivin tulostus väärin.')

if __name__ == '__main__':
    unittest.main()

