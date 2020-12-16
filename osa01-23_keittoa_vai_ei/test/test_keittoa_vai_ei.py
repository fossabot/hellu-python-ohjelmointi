import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.keittoa_vai_ei'

def parse_result(output):
    if len(output) > 30:
        return output[:30] + "..."
    else:
        return output

def oikea_jarjestys(output):
    parts = output.split("\n")
    hinta = False
    for part in parts:
        if 'Kokonaishinta on' in part:
            hinta = True
        if "Seuraava!" == part and not hinta:
            return False

    return True  

@points('1.keittoa_vai_ei')
class KeittoaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_kramer_1(self):
        with patch('builtins.input', side_effect = [ 'Kramer', '1', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            expected = "Seuraava!"
            self.assertTrue(expected in output, f"Syötteellä Kramer, 1 ohjelmasi pitäisi tulostaa \n{expected}\nohjelmasi tulosti\n"+ output)
            expected = 'Kokonaishinta on 5.9'
            self.assertTrue(expected in output, f"Syötteellä Kramer, 1 ohjelmasi pitäisi tulostaa \n{expected}\nohjelmasi tulosti\n"+ output)
            self.assertTrue(oikea_jarjestys(output), f"Syötteellä Kramer, 1 ohjelmasi pitäisi tulostaa \n'Seuraava' vasta hinnan ilmoittamisen jälkeen\nohjelmasi tulosti\n"+ output)


    def test_kramer_4(self):
        with patch('builtins.input', side_effect = [ 'Kramer', '4', AssertionError("Syötettä pyydetään liian monta kertaa.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            expected = "Seuraava!"
            self.assertTrue(expected in output, f"Syötteellä Kramer, 4 ohjelmasi pitäisi tulostaa \n{expected}\nohjelmasi tulosti\n"+ output)
            expected = 'Kokonaishinta on 23.6'
            self.assertTrue(expected in output, f"Syötteellä Kramer, 4 ohjelmasi pitäisi tulostaa \n{expected}\nohjelmasi tulosti\n"+ output)
            self.assertTrue(oikea_jarjestys(output), f"Syötteellä Kramer, 4 ohjelmasi pitäisi tulostaa \n'Seuraava' vasta hinnan ilmoittamisen jälkeen\nohjelmasi tulosti\n"+ output)

    def test_jerry(self):
        with patch('builtins.input', side_effect = [ 'Jerry', AssertionError("Syötettä pyydetään liian monta kertaa kun nimeksi ilmoitetaan Jerry.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            expected = "Seuraava!"
            self.assertTrue(expected in output, f"Syötteellä Jerry ohjelmasi pitäisi tulostaa \n{expected}\nohjelmasi tulosti\n"+ output)

    def test_jane_doe(self):
        with patch('builtins.input', side_effect = [ 'Jane Doe', '2', AssertionError("Syötettä pyydetään liian monta kertaa kun nimeksi ilmoitetaan Jane Doe.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            expected = "Seuraava!"
            self.assertTrue(expected in output, f"Syötteellä Jane Doe, 2 ohjelmasi pitäisi tulostaa \n{expected}\nohjelmasi tulosti\n"+ output)
            expected = 'Kokonaishinta on 11.8'
            self.assertTrue(expected in output, f"Syötteellä Jane Doe, 2 ohjelmasi pitäisi tulostaa \n{expected}\nohjelmasi tulosti\n"+ output)

    if False:

        def test_lisatestit(self):
            testset = ['-99', '4', '435634', '-234', '6', '0']
            for luku in testset:
                with patch('builtins.input', return_value = luku):
                    reload_module(self.module)
                    result = luku[1:-1] if int(luku)<0 else luku
                    self.assertTrue(result in get_stdout(), 'Ohjelmasi toimii väärin syötteellä ' + luku + '. Vastauksen tulisi olla ' + result)

if __name__ == '__main__':
    unittest.main()
