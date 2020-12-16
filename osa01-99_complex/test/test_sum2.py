import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_stdout

class OutputTest(unittest.TestCase):

  def test_sum(self):
    with patch('builtins.input', side_effect=['1', '2']) as prompt:
      from src.sum2 import main 
      main()
      output = get_stdout()
      self.assertTrue("summa 3" in output, " "+ output)

    with patch('builtins.input', side_effect=['3', '5']) as prompt:
      from src.sum2 import main 
      main()
      output = get_stdout()
      self.assertTrue("summa 8" in output, " "+ output)
