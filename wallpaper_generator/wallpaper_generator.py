from PIL import Image, ImageDraw
from os import listdir
from os.path import isfile, isdir, join, splitext, exists, basename
import tkinter
import argparse


class WallpaperGenerator:
  def __init__(self):
    self.args = None
    self.init_args()
    self.dir_or_file()

  def valid_path(self, path):
    if not exists(path):
      raise argparse.ArgumentTypeError('%s is not a valid path' % path)
    return path

  def valid_dimension(self, dimension):
    d = int(dimension)
    if 0 >= d:
      raise argparse.ArgumentTypeError(
          '%s is not a valid dimension' % d)
    return d

  def init_args(self):
    arg_parser = argparse.ArgumentParser(
        description='A script that generates wallpapers from images')

    arg_parser.add_argument(
        'src_path', type=self.valid_path, help='Path of a directory with images or a single image to process')
    arg_parser.add_argument('--dest_path', type=self.valid_path, default='.', metavar='', 
                                 help='Path of a directory where a result of the script will be saved, defaultly it\'s a current working directory')
    arg_parser.add_argument(
        '--i_min_w', type=self.valid_dimension, default=0, metavar='', help='Min width of an input image')
    arg_parser.add_argument(
        '--i_min_h', type=self.valid_dimension, default=0, metavar='', help='Min height of an input image')
    arg_parser.add_argument(
        '--i_max_w', type=self.valid_dimension, default=2147483647, metavar='', help='Max width of an input image')
    arg_parser.add_argument(
        '--i_max_h', type=self.valid_dimension, default=2147483647, metavar='', help='Max height of an input image')
    root = tkinter.Tk()
    arg_parser.add_argument(
        '--o_w', type=self.valid_dimension, default=root.winfo_screenwidth(), metavar='', help='Width of an output wallpaper')
    arg_parser.add_argument(
        '--o_h', type=self.valid_dimension, default=root.winfo_screenheight(), metavar='', help='Height of an output wallpaper')
    
    self.args = arg_parser.parse_args()

  def dir_or_file(self):
    if isdir(self.args.src_path):
      self.iterate_over_files()
    else:
      if self.check_if_img(self.args.src_path):
        self.generate_wallpaper(self.args.src_path)
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
      self.generate_wallpaper(join(self.args.src_path, img))

  def check_if_img(self, path):
    return splitext(path)[1] in ['.jpg', '.png', '.bmp', '.gif']

  def generate_wallpaper(self, img_path):
    img = Image.open(img_path).convert('RGB')
    if self.check_img_dimensions(img):
      colors = self.get_colors(img)
      img_g = self.gradient(colors)
      wallpaper = self.compose_imgs(img, img_g)
      self.save_wallpaper(img_path, wallpaper)

  def check_img_dimensions(self, img):
    if img.width < self.args.i_min_w or img.height < self.args.i_min_h:
      print('The image is too small')
      return False
    if img.width > self.args.i_max_w or img.height > self.args.i_max_h:
      print('The image is too big')
      return False
    return True

  def get_colors(self, img):
    img_w = img.width
    img_h = img.height
    return sorted(img.getcolors(
        img_w * img_h), key=lambda x: x[0])[-2:]

  def gradient(self, colors):
    w = self.args.o_w
    h = self.args.o_h
    c = colors

    img_g = Image.new('RGB', (w, h), '#FFFFFF')
    draw = ImageDraw.Draw(img_g)

    r, g, b = c[0][1]
    _r, _g, _b = (x / h * c[0][0] / c[1][0] for x in c[1][1])
    for i in range(h):
      r, g, b = r + _r, g + _g, b + _b
      draw.line((0, i, w, i), fill=(int(r), int(g), int(b)))

    return img_g

  def compose_imgs(self, img, img_g):
    offset = ((img_g.width - img.width) // 2,
              (img_g.height - img.height) // 2)
    img_g.paste(img, offset)
    return img_g

  def save_wallpaper(self, img_path, wallpaper):
    path = splitext(basename(img_path))
    path = join(self.args.dest_path, '{}_wallpaper{}'.format(path[0], path[1]))
    wallpaper.save(path)
    print('Saved as: {}'.format(path))


def main():
  wallpaperGenerator = WallpaperGenerator()


if __name__ == '__main__':
  main()
