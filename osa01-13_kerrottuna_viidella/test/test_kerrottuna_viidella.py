import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.kerrottuna_viidella'

@points('1.kerrottuna_viidella')
class KerrottunaViidellaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_kerrottuna_kolmella(self):
        with patch('builtins.input', return_value = '3'):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue('15' in output, 'Tuloste ei toimi oikein syötteellä 3., ohjelmsi tulostaa\n' + output)
            expected = 'Kun kerrotaan 3 luvulla 5, saadaan 15'
            self.assertTrue(expected in output, 'Ohjelmasi tulostus ei ole oikea syötteellä 3. Sen pitäisi olla\n'+expected+'\nOhjelmasi tulostaa\n'+ output)

    def test_kerrottuna_viidella(self):
        with patch('builtins.input', return_value = '5'):
            reload_module(self.module)
            output = get_stdout()
            expected = 'Kun kerrotaan 5 luvulla 5, saadaan 25'
            self.assertTrue(expected in output, 'Ohjelmasi tulostus ei ole oikea syötteellä 5. Sen pitäisi olla\n'+expected+'\nOhjelmasi tulostaa\n'+ output)
   
    def test_kerrottuna_sadalla(self):
        with patch('builtins.input', return_value = '100'):
            reload_module(self.module)
            output = get_stdout()
            expected = 'Kun kerrotaan 100 luvulla 5, saadaan 500'
            self.assertTrue(expected in output, 'Ohjelmasi tulostus ei ole oikea syötteellä 100. Sen pitäisi olla\n'+expected+'\nOhjelmasi tulostaa\n'+ output)

    def test_lukua_kysytaan_tasmalleen_kerran(self):
        with patch('builtins.input', return_value = '0') as prompt:
            reload_module(self.module)
            output = get_stdout()
            try:
                prompt.assert_called_once()
            except AssertionError:
                self.fail('Syötettä tulee pyytää täsmälleen kerran.')

if __name__ == '__main__':
    unittest.main()
