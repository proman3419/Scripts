from PIL import Image, ImageDraw
from os import listdir
from os.path import isfile, isdir, join, splitext, exists, basename
import tkinter
import sys


class WallpaperGenerator:
  def __init__(self):
    if not self.check_if_args_passed():
      self.get_screen_res()
    self.dir_or_file()

  def check_if_args_passed(self):
    try:
      self.path = sys.argv[1]
    except IndexError:
      print('File\'s/directory\'s path has not been specified')
      exit()
    try:
      self.width = int(sys.argv[2])
      self.height = int(sys.argv[3])

      if self.width <= 0 or self.height <= 0:
        return False
      return True
    except (IndexError, ValueError):
      return False

  def get_screen_res(self):
    root = tkinter.Tk()
    self.width = root.winfo_screenwidth()
    self.height = root.winfo_screenheight()

  def dir_or_file(self):
    if exists(self.path):
      if isdir(self.path):
        files = [f for f in listdir(self.path) if isfile(join(self.path, f))]

        if len(files) == 0:
          print('No files have been found in the passed directory')

        i = 1
        for f in files:
          print('[{}/{}] Current file: {}'.format(i,
                                                  len(files),
                                                  join(self.path, f)))
          self.file_path = join(self.path, f)
          self.generate_wallpaper()
          i += 1
      elif isfile(self.path):
        self.file_path = self.path
        self.generate_wallpaper()
    else:
      print('The passed path doesn\'t exist')

  def generate_wallpaper(self):
    if self.check_if_img():
      self.open_img()
      self.get_colors()
      self.gradient()
      self.compose_imgs()
      self.save_img()

  def check_if_img(self):
    if splitext(self.file_path)[1] in ['.jpg', '.png', '.bmp', '.gif']:
      print('File is an image')
      return True
    else:
      print('File isn\'t an image')
      return False

  def open_img(self):
    self.img = Image.open(self.file_path)
    self.img = self.img.convert('RGB')

  def get_colors(self):
    im_w = self.img.width
    im_h = self.img.height
    self.colors = sorted(self.img.getcolors(
        im_w * im_h), key=lambda x: x[0])[-2:]

  def gradient(self):
    w = self.width
    h = self.height
    c = self.colors

    self.img_g = Image.new('RGB', (w, h), '#FFFFFF')
    draw = ImageDraw.Draw(self.img_g)

    r, g, b = c[0][1]
    _r, _g, _b = (x / h * c[0][0] / c[1][0] for x in c[1][1])
    for i in range(h):
      r, g, b = r + _r, g + _g, b + _b
      draw.line((0, i, w, i), fill=(int(r), int(g), int(b)))

  def compose_imgs(self):
    offset = ((self.img_g.width - self.img.width) // 2,
              (self.img_g.height - self.img.height) // 2)
    self.img_g.paste(self.img, offset)

  def save_img(self):
    name = basename(self.file_path)
    name = splitext(name)
    name = '{}_wallpaper{}'.format(name[0], name[1])
    self.img_g.save(name)
    print('Saved as: {}'.format(name))


def main():
  wallpaperGenerator = WallpaperGenerator()


if __name__ == '__main__':
  main()
