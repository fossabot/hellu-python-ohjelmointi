import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_stdout
Summer = load('src.summer', 'Summer')

class OutputTest(unittest.TestCase):

  def test_sum(self):
    with patch('builtins.input', side_effect=['1', '2']) as prompt:
      s = Summer()
      s.main()
      output = get_stdout()
      self.assertTrue("summa 3" in output, " "+ output)

  def test_sums(self):
    inputs = [('3', '4'), ('7', '12'), ('8', '11'), ('-32', '21')]
    for x, y in inputs:
      with patch('builtins.input', side_effect=[ x, y ]) as prompt:
        s = Summer()
        s.main()
        output = get_stdout()
        sum = int(x) + int(y)
        self.assertTrue("summa "+str(sum) in output, " "+ output)

