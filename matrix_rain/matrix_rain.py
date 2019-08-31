import shutil
import random
import time
import keyboard
import os
import argparse


class Column:
  def __init__(self):
    self.spaces_amount = 0
    self.chars_amount = 0
    self.content = []

  def update_amounts(self, w, h, min_cd, max_cd, min_sd, max_sd):
    r = random.randint(0, 100)
    if r < 50:
      self.chars_amount = random.randint(
        int(h * min_cd), int(h * max_cd))
    else:
      self.spaces_amount = random.randint(
        int(h * min_sd), int(h * max_sd))

  def push_char(self):
    if self.spaces_amount > 0:
      self.content.insert(0, ' ')
      self.spaces_amount -= 1
    else:
      # 33-126 printable ASCII chars
      self.content.insert(0, chr(random.randint(33, 126)))
      self.chars_amount -= 1

  def update(self, w, h, min_cd, max_cd, min_sd, max_sd):
    if self.spaces_amount == self.chars_amount == 0:
      self.update_amounts(w, h, min_cd, max_cd, min_sd, max_sd)
    self.push_char()
    if len(self.content) >= h:
      self.content.pop()


class MatrixRain:
  def __init__(self):
    self.width = self.height = 0
    self.columns = []
    self.color = '\033[1;32;40m'
    self.args = []
    self.init_arg_parser()
    self.setup()

  def valid_speed(self, speed):
    v = float(speed)
    if v < 1 or 100 < v:
      raise argparse.ArgumentTypeError('%s is not a valid speed value' % speed)
      return None
    return v

  def valid_percent(self, percent):
    p = float(percent)
    if p < 0.01 or 1 < p:
      raise argparse.ArgumentTypeError('%s is not in a valid values range' % percent)
      return None
    return p

  def valid_min_max(self, _min, _max, _min_name, _max_name):
    if _min > _max:
      print('{} was greater than {}. A min value should be smaller than max value'.format(_min_name, _max_name))
      exit()

  def init_arg_parser(self):
    self.arg_parser = argparse.ArgumentParser(
        description='''In order to exit the script press BACKSPACE.
The script should be run as root in order to capture a BACKSPACE press.
In brackets next to arguments names there is info about: <range> {default value}.

Will you pick the red pill or the blue pill?''', formatter_class=argparse.RawTextHelpFormatter)

    self.arg_parser.add_argument(
        '--speed', type=self.valid_speed, nargs='?', const=1, default=25, metavar='<1 - 100> {25}', help='speed of falling characters')
    self.arg_parser.add_argument(
        '--min_cd', type=self.valid_percent, nargs='?', const=1, default=0.1, metavar='<0.01 - 1.0> {0.1}', help='min characters density')
    self.arg_parser.add_argument(
        '--max_cd', type=self.valid_percent, nargs='?', const=1, default=0.2, metavar='<0.01 - 1.0> {0.2}', help='max characters density')
    self.arg_parser.add_argument(
        '--min_sd', type=self.valid_percent, nargs='?', const=1, default=0.3, metavar='<0.01 - 1.0> {0.3}', help='min spaces density')
    self.arg_parser.add_argument(
        '--max_sd', type=self.valid_percent, nargs='?', const=1, default=0.4, metavar='<0.01 - 1.0> {0.4}', help='max spaces density')
    
    self.args = self.arg_parser.parse_args()
    self.valid_min_max(self.args.min_cd, self.args.max_cd, 'min_cd', 'max_cd')
    self.valid_min_max(self.args.min_sd, self.args.max_sd, 'min_sd', 'max_sd')

  def setup(self):
    self.width, self.height = shutil.get_terminal_size()
    self.columns = [Column() for x in range(self.width)]
    for col in self.columns:
      col.content = [' ' for y in range(self.height)]

  def draw(self):
    for col in self.columns:
      col.update(self.width, self.height, self.args.min_cd, self.args.max_cd, self.args.min_sd, self.args.max_sd)
    self.print_columns()
    time.sleep(1 / self.args.speed)

  def print_columns(self):
    to_print = ''
    for y in range(self.height):
      for x in range(self.width):
        to_print += str(self.columns[x].content[y])
    to_print += self.color # add color to the output
    print(to_print)

  def check_if_exit(self):
    try:
      if keyboard.is_pressed('backspace'):
        self.clear_screen()
        exit()
    except ImportError:
      print('You need to run the script as root')
      exit()

  def clear_screen(self):
    try:
      os.system('clear')
    except:
      os.system('cls')


def main():
  m_r = MatrixRain()
  while True:
    m_r.draw()
    m_r.check_if_exit()


if __name__ == '__main__':
  main()