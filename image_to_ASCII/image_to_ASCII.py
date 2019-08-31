from PIL import Image
from os.path import isfile, join, splitext, exists, basename
import argparse


class Converter:
  def __init__(self):
    self.args = []
    self.img = None
    self.r = []
    self.init_args()
    if self.check_if_img():
      self.open_img()
      self.to_ASCII()
      self.save_to_file()

  def valid_path(self, path):
    if not exists(path):
      raise argparse.ArgumentTypeError('%s is not a valid path' % path)
    return path

  def valid_scale(self, scale):
    s = int(scale)
    if s <= 0:
      raise argparse.ArgumentTypeError('The scale is too small')
    if s > 500:
      raise argparse.ArgumentTypeError('The scale is too big')
    return s

  def init_args(self):
    arg_parser = argparse.ArgumentParser(
        description='''asdf''', formatter_class=argparse.RawTextHelpFormatter)

    arg_parser.add_argument(
        'src_path', type=self.valid_path, help='Path of a directory with images or a single image to process')
    arg_parser.add_argument('--dest_path', type=self.valid_path, default='.', metavar='', 
                                 help='Path of a directory where a result of the script will be saved, defaultly it\'s a current working directory')
    arg_parser.add_argument('--scale', type=self.valid_scale, default=100, metavar='', 
                                 help='Scale of the outputed text image')

    self.args = arg_parser.parse_args()

  def check_if_img(self):
    if isfile(self.args.src_path):
      if splitext(self.args.src_path)[1] in ['.jpeg', '.jpg', '.png', '.bmp', '.gif']:
        return True
    print('The passed source path doesn\'t contain an image')
    return False

  def open_img(self):
    self.img = Image.open(self.args.src_path)
    self.img = self.img.convert('L')
    wh_font_ratio = 0.526
    self.img = self.img.resize(
        (self.args.scale, 
         int(self.img.height * self.args.scale * wh_font_ratio / self.img.width)))

  def to_ASCII(self):
    chars = r'$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`". '

    for px in list(self.img.getdata()):
      self.r.append(chars[int(px / 255 * (len(chars) - 1))])

  def save_to_file(self):
    name = basename(self.args.src_path)
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
