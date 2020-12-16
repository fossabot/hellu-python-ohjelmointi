import unittest
from unittest.mock import patch
import importlib
from tmc import points

from tmc.utils import load, get_stdout

class OutputTest(unittest.TestCase):

  def test_sum1(self):
    with patch('builtins.input', side_effect=['8', '4']) as prompt:
      module = importlib.import_module('src.sum')
      output = get_stdout()
      self.assertTrue("Ryhmien määrä: 2" in output, " "+ output)  
      del module

  def test_sum2(self):
    with patch('builtins.input', side_effect=['11', '3']) as prompt:
      module = importlib.import_module('src.sum')
      output = get_stdout()
      self.assertEqual("Ryhmien määrä: 4", output, " "+output)  
      del module

