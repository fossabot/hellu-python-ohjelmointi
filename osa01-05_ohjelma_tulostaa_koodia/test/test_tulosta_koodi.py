import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.tulosta_koodi'

@points('1.tulosta_koodi')
class TulostaKoodiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(exercise, 'fi')

    def test_tulostus(self):
        reload_module(self.module)
        output = get_stdout()
        split_output = output.split('\n')

        self.assertEqual(len(split_output), 1, "Tulostuksessa on ylimääräisiä rivejä.")
        self.assertTrue(output.count('print') == 1, "Tulostuksesta puuttuu print-komento.")
        self.assertTrue(output.count('"') == 2, "Lainausmerkit puuttuvat tulostuksesta.")
        self.assertEqual(output, 'print("Moi kaikki!")', "Tulostus ei ole oikein.")

if __name__ == '__main__':
    unittest.main()
