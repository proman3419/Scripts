# Wallpaper generator

The script picks two most used colors in an image and creates a gradient out of them. This activity is followed with adding the image centered on the gradient.

![alt text](https://github.com/proman3419/Scripts-and-tools/blob/master/wallpaper_generator/screenshot_1.png)

![alt text](https://github.com/proman3419/Scripts-and-tools/blob/master/wallpaper_generator/screenshot_2.png)

## Requirements
* Python 3.x
* Pillow 5.4.1

## Usage
```
usage: wallpaper_generator.py [-h] [--dest_path [DEST_PATH]]
                              [--i_min_w [I_MIN_W]] [--i_min_h [I_MIN_H]]
                              [--i_max_w [I_MAX_W]] [--i_max_h [I_MAX_H]]
                              [--o_w [O_W]] [--o_h [O_H]]
                              source_path

A script that generates wallpapers from images

positional arguments:
  source_path           path of a directory with images or a single image to
                        process

optional arguments:
  -h, --help            show this help message and exit
  --dest_path [DEST_PATH]
                        path of a directory where a result of the script will
                        be saved, defaultly it's a current working directory
  --i_min_w [I_MIN_W]   min width of an input image
  --i_min_h [I_MIN_H]   min height of an input image
  --i_max_w [I_MAX_W]   max width of an input image
  --i_max_h [I_MAX_H]   max height of an input image
  --o_w [O_W]           width of an output wallpaper
  --o_h [O_H]           height of an output wallpaper
```