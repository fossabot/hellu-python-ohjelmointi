import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.nimi_ja_huutomerkit'

@points('1.nimi_ja_huutomerkit')
class NimiJaHuutomerkkiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = ''):
            cls.module = load_module(exercise, 'fi')

    def test_syotteen_tulostus_1(self):
        with patch('builtins.input', return_value = 'Pekka'):
            reload_module(self.module)
            output = get_stdout()
            self.assertEqual(output, '!Pekka!Pekka!', 'Tuloste ei toiminut oikein syötteellä: Pekka')

    def test_syotteen_tulostus_2(self):
        with patch('builtins.input', return_value = 'Ada'):
            reload_module(self.module)
            output = get_stdout()
            self.assertEqual(output, '!Ada!Ada!', 'Tuloste ei toiminut oikein syötteellä: Ada.')

    def test_syotetta_kysytaan_tasmalleen_kerran(self):
        with patch('builtins.input', return_value = '') as prompt:
            reload_module(self.module)
            output = get_stdout()
            try:
                prompt.assert_called_once()
            except AssertionError:
                self.fail('Syötettä tulee pyytää täsmälleen kerran.')

if __name__ == '__main__':
    unittest.main()
