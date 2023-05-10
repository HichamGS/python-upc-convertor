import unittest
from upc_digit_calc import CheckDigitCalc

#test object
raint = 64290553937
test_obj = CheckDigitCalc()
test_obj.input_str = str(raint)

class TestUPCConvertor(unittest.TestCase):
  def test_check_digit_length(self):
    self.assertEqual(len(test_obj.input_str), 11)

  def test_check_digit_integer(self):
    test_obj.check_digit_integer()
    self.assertEqual(test_obj.input_int, raint)

if __name__ == '__main__':
  unittest.main()

