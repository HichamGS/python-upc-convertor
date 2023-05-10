from random import randint
import pandas as pd

def rand_11_digits_upc():
  upc_s = ''.join(["%s" % randint(0,9) for n in range(0,11)])
  return upc_s


class CheckDigitCalc:
  def __init__(self):
    self.input_str = None
    self.input_int = None
    self.check_digit = None
    self.odd_sum = None
    self.odd_sum_3_times = None
    self.sum_even = None
    self.modulo = None
    self.sum = None
    self.modulo = None
    self.check_digit = None

  def check_digit_length(self):
    if len(self.input_str) == 11:
      return True
    else:
      return False

  def check_digit_integer(self):
    try: 
      self.input_int = int(self.input_str)
    except ValueError:
      print('The entered string is not exclusively numeric !')

  def calc_sum_odd(self):
    self.odd_sum = sum(int(self.input_str[i]) for i,j in enumerate(self.input_str) if i % 2 == 0)

  def calc_3_times_odd_sum(self):
    self.odd_sum_3_times = 3 * self.odd_sum

  def calc_sum_even(self):
    self.sum_even = sum(int(self.input_str[i]) for i, j in enumerate(self.input_str) if i % 2 != 0)
    self.sum = self.sum_even + self.odd_sum_3_times

  def calc_modulo(self):
    self.modulo = self.sum % 10

  def check_digit_number(self):
    if self.modulo == 10:
      self.check_digit = 0
    else:
      self.check_digit = 10 - self.modulo


  def compute_check_digit(self, input_upc):
    self.input_str = input_upc
    if self.check_digit_length():
      self.check_digit_integer()
      self.calc_sum_odd()
      self.calc_3_times_odd_sum()
      self.calc_sum_even()
      self.calc_modulo()
      self.check_digit_number()
      return self.check_digit
    else:
      return ''

  def get_full_upc(self, input_upc):
    self.input_str = input_upc
    return self.input_str + str(self.compute_check_digit(input_upc))



class ProcessCSVRawData(CheckDigitCalc):
  def __init__(self):
    super().__init__
    self.input_file_path = None
    self.input_file = None
    self.output_file_path = None
    self.output_file = None
    self.upc_column = 'REFCODE'
    self.upc_df = pd.DataFrame()
    self.upc_list = None
    self.updated_upcs = None


  def read_file_info(self, input_file_path, input_file):
    self.input_file_path = input_file_path
    self.input_file = input_file
    self.upc_df = pd.read_csv(
      self.input_file_path + self.input_file,
      dtype={self.upc_column: str}, na_filter=False,
      usecols=['DESCRIPTION', 'REFCODE']
    )
    
  def update_upc_df(self):
    self.upc_list = list(self.upc_df[self.upc_column])
    self.updated_upcs = [(x + str(self.compute_check_digit(x))) for x in self.upc_list]
    self.upc_df[self.upc_column] = self.updated_upcs

  def write_upc_csv(self, output_file_path, output_file):
    self.output_file_path = output_file_path
    self.output_file = output_file
    self.upc_df.to_csv(self.output_file_path + self.output_file, index=False)
    


if __name__ == '__main__': 
  upc_s = rand_11_digits_upc()
  obj = CheckDigitCalc()
  print(obj.get_full_upc(upc_s))

  # obj = ProcessCSVRawData()
  # obj.read_file_info('./', 'refs.csv');
  # obj.update_upc_df()
  # obj.write_upc_csv('./', 'refs-updated.csv')

