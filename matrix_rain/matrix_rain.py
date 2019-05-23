import shutil
import random
import time
import keyboard
import os
from sys import argv


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
    self.speed = self.arg_parser(1, 100, 1, default_v=30)
    self.min_cd = self.arg_parser(0.05, 1, 2, default_v=0.1) # cd = characters density
    self.max_cd = self.arg_parser(0.05, 1, 3, default_v=0.2)
    self.min_sd = self.arg_parser(0.05, 1, 4, default_v=0.3) # sd = spaces density
    self.max_sd = self.arg_parser(0.05, 1, 5, default_v=0.4)

    # Replace min and max values if they were passed in a wrong order
    self.min_cd, self.max_cd = self.replace_min_max(self.min_cd, self.max_cd)
    self.min_sd, self.max_sd = self.replace_min_max(self.min_sd, self.max_sd)

    self.setup()

  def setup(self):
    self.width, self.height = shutil.get_terminal_size()
    self.columns = [Column() for x in range(self.width)]
    for col in self.columns:
      col.content = [' ' for y in range(self.height)]

  def arg_parser(self, min_v, max_v, id, default_v):
    try:
      x = float(argv[id])
      if min_v <= x <= max_v:
        return x
      else:
        return default_v
    except:
      return default_v

  def replace_min_max(self, min_v, max_v):
    return (max_v, min_v) if min_v > max_v else (min_v, max_v)

  def draw(self):
    for col in self.columns:
      col.update(self.width, self.height, self.min_cd, self.max_cd, self.min_sd, self.max_sd)
    self.print_columns()
    time.sleep(1 / self.speed)

  def print_columns(self):
    to_print = ''
    for y in range(self.height):
      for x in range(self.width):
        to_print += str(self.columns[x].content[y])
    to_print += self.color # add font's color to the output
    print(to_print)

  def check_if_exit(self):
    if keyboard.is_pressed('backspace'):  # if key 'q' is pressed 
      self.clear_screen()
      exit()
    else:
      pass

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