import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_stdout
Output = load('src.output_first', '')

class OutputTest(unittest.TestCase):

    def test_output(self):
        import src.first_output
        output = get_stdout()
        self.assertTrue("Se pyörii sittenkin!" in output, "Ohjelma tulostaa oikean viestin.")
        
