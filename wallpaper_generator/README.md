# Wallpaper generator

The script picks two most used colors in an image and creates a gradient out of them. This activity is followed by adding the image centered on the gradient.

![alt text](https://github.com/proman3419/Scripts-and-tools/blob/master/wallpaper_generator/screenshot_1.png)

![alt text](https://github.com/proman3419/Scripts-and-tools/blob/master/wallpaper_generator/screenshot_2.png)

## Usage
```
usage: wallpaper_generator.py [-h] [--dest_path {.}] [--i_min_w] [--i_min_h]
                              [--i_max_w] [--i_max_h]
                              [--o_w {device's screen width}]
                              [--o_h {device's screen height}]
                              src_path

This script generates wallpapers from images.
Next to arguments names there is info about: <range> {default value}.

positional arguments:
  src_path              Path of a directory with images or a single image to process

optional arguments:
  -h, --help            show this help message and exit
  --dest_path {.}       Path of a directory where a result of the script will be saved
  --i_min_w             Min width of an input image
  --i_min_h             Min height of an input image
  --i_max_w             Max width of an input image
  --i_max_h             Max height of an input image
  --o_w {device's screen width}
                        Width of an output wallpaper
  --o_h {device's screen height}
                        Height of an output wallpaper
```