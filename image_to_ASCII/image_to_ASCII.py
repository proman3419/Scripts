from PIL import Image
from os.path import isfile, join, splitext, exists, basename
import sys


class Converter:
  def __init__(self):
    self.check_if_arg_passed()
    if self.check_if_valid_scale():
      if self.check_if_img():
        self.open_img()
        self.to_ASCII()
        self.save_to_file()

  def check_if_arg_passed(self):
    try:
      self.path = sys.argv[1]
      try:
        self.scale = int(sys.argv[2])
      except IndexError:
        self.scale = 100  
    except IndexError:
      print('File\'s path has not been specified')
      exit()

  def check_if_valid_scale(self):
    if self.scale >= 500:
      print('The scale should be smaller than 500')
    elif self.scale <= 0:
      print('The scale should be a positive integer')
    else:
      return True

  def check_if_img(self):
    if exists(self.path):
      if isfile(self.path):
        if splitext(self.path)[1] in ['.jpeg', '.jpg', '.png', '.bmp', '.gif']:
          print('File is an image')
          return True
        else:
          print('File isn\'t an image')
      else:
        print('The passed path doesn\'t point a file')
    else:
      print('The passed path doesn\'t exist')

  def open_img(self):
    self.img = Image.open(self.path)
    self.img = self.img.convert('L')
    wh_font_ratio = 0.526
    self.img = self.img.resize(
        (self.scale, 
         int(self.img.height * self.scale * wh_font_ratio / self.img.width)))

  def to_ASCII(self):
    chars = r'$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`". '
    self.r = []

    for px in list(self.img.getdata()):
      self.r.append(chars[int(px / 255 * (len(chars) - 1))])

  def save_to_file(self):
    name = basename(self.path)
    name = splitext(name)
    name = '{}_ASCII.txt'.format(name[0])
    with open(name, 'w') as f:
      f.write('\n'.join([''.join(self.r[i:i + self.img.width])
                         for i in range(0, len(self.r), self.img.width)]))
    print('Saved as: {}'.format(name))


def main():
  converter = Converter()


if __name__ == '__main__':
  main()
