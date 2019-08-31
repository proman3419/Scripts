# Wallpaper generator

The script picks two most used colors in an image and creates a gradient out of them. This activity is followed by adding the image centered on the gradient.

![alt text](https://github.com/proman3419/Scripts-and-tools/blob/master/wallpaper_generator/screenshot_1.png)

![alt text](https://github.com/proman3419/Scripts-and-tools/blob/master/wallpaper_generator/screenshot_2.png)

## Requirements
* Python 3.x
* Pillow 5.4.1

## Usage
```
usage: wallpaper_generator.py [-h] [--dest_path] [--i_min_w] [--i_min_h]
                              [--i_max_w] [--i_max_h] [--o_w] [--o_h]
                              source_path

A script that generates wallpapers from images

positional arguments:
  source_path   Path of a directory with images or a single image to process

optional arguments:
  -h, --help    show this help message and exit
  --dest_path   Path of a directory where a result of the script will be
                saved, defaultly it's a current working directory
  --i_min_w     Min width of an input image
  --i_min_h     Min height of an input image
  --i_max_w     Max width of an input image
  --i_max_h     Max height of an input image
  --o_w         Width of an output wallpaper
  --o_h         Height of an output wallpaper
```