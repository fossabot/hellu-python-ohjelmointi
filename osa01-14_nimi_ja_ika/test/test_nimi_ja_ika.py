import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.nimi_ja_ika'

def parse_result(output):
    if len(output) > 30:
        return output[:30] + "..."
    else:
        return output

@points('1.nimi_ja_ika')
class NimiJaIkaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_keijo_keksitty(self):
        with patch('builtins.input', side_effect = [ 'Keijo Keksitty', '1990', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue('Moi Keijo Keksitty, olet 30 vuotta vanha vuoden 2020 lopussa' in output, "Ohjelmasi olisi pitänyt tulostaa 'Moi Keijo Keksitty, olet 30 vuotta vanha vuoden 2020 lopussa'. \nOhjelmasi tulosti:\n" + output)

    def test_muita_nimia(self):
        testset = [
            ['Pekka Python', '2019', '1'],
            ['Angela Merkel', '1954', '66'],
            ['Venla Ruuska', '2013', '7'],
        ]
        for nimi, syntvuosi, ika in testset:
            with patch('builtins.input', side_effect = [nimi, syntvuosi]):
                reload_module(self.module)
                expected = f"Moi {nimi}, olet {ika} vuotta vanha vuoden 2020 lopussa"
                self.assertTrue(expected in get_stdout(), 'Ohjelmasi toimii väärin syötteellä {nimi} ja {syntvuosi}. Vastauksen tulisi olla ' + expected)

if __name__ == '__main__':
    unittest.main()
