from PIL import Image
from os import listdir
from os.path import isfile, isdir, join, splitext, exists, basename
import argparse


class Converter:
  def __init__(self):
    self.args = []
    self.r = []
    self.init_args()
    self.dir_or_file()

  def valid_path(self, path):
    if not exists(path):
      raise argparse.ArgumentTypeError('%s is not a valid path' % path)
    return path

  def valid_scale(self, scale):
    s = int(scale)
    if s < 1:
      raise argparse.ArgumentTypeError('The scale is too small')
    if s > 500:
      raise argparse.ArgumentTypeError('The scale is too big')
    return s

  def init_args(self):
    arg_parser = argparse.ArgumentParser(
        description='''This script changes images to text files.
Next to arguments names there is info about: <range> {default value}.''', formatter_class=argparse.RawTextHelpFormatter)

    arg_parser.add_argument(
        'src_path', type=self.valid_path, help='Path of a directory with images or a single image to process')
    arg_parser.add_argument('--dest_path', type=self.valid_path, default='.', metavar='{.}', 
                                 help='Path of a directory where a result of the script will be saved')
    arg_parser.add_argument('--scale', type=self.valid_scale, default=100, metavar='<1 - 500> {100}', 
                                 help='Scale of the outputed text image')

    self.args = arg_parser.parse_args()

  def dir_or_file(self):
    if isdir(self.args.src_path):
      self.iterate_over_files()
    else:
      if self.check_if_img(self.args.src_path):
        self.generate_ascii_image(self.args.src_path)
      else:
        print('The source path doesn\'t contain an image')

  def iterate_over_files(self):
    imgs = [f for f in listdir(self.args.src_path) if isfile(join(self.args.src_path, f))
            and self.check_if_img(f)]

    if not imgs:
      print('No images have been found in the source path')

    imgs_len = len(imgs)
    for i, img in enumerate(imgs):
      print('[{}/{}] Current image: {}'.format(i + 1,
                                               imgs_len,
                                               join(self.args.src_path, img)))
      self.generate_ascii_image(join(self.args.src_path, img))

  def check_if_img(self, path):
    return splitext(path)[1] in ['.jpg', '.png', '.bmp', '.gif']

  def generate_ascii_image(self, img_path):
    img = self.open_img(img_path)
    r = self.to_ascii(img)
    self.save_to_file(img, img_path, r)

  def open_img(self, img_path):
    img = Image.open(img_path).convert('L')
    wh_font_ratio = 0.526
    return img.resize(
        (self.args.scale, 
         int(img.height * self.args.scale * wh_font_ratio / img.width)))

  def to_ascii(self, img):
    chars = r'$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`". '
    r = []
    for px in list(img.getdata()):
      r.append(chars[int(px / 255 * (len(chars) - 1))])
    return r

  def save_to_file(self, img, img_path, r):
    path = splitext(basename(img_path))
    path = join(self.args.dest_path, '{}_ASCII.txt'.format(path[0]))
    with open(path, 'w') as f:
      f.write('\n'.join([''.join(r[i:i + img.width])
                         for i in range(0, len(r), img.width)]))
    print('Saved as: {}'.format(path))


def main():
  converter = Converter()


if __name__ == '__main__':
  main()
