# Image to ASCII

![alt text](https://github.com/proman3419/Scripts-and-tools/blob/master/image_to_ASCII/screenshot.png)

## Requirements
* Python 3.x
* Pillow 5.4.1

## Usage
```
usage: image_to_ASCII.py [-h] [--dest_path {.}] [--scale <1 - 500> {100}]
                         src_path

This script changes images to text files.
Next to arguments names there is info about: <range> {default value}.

positional arguments:
  src_path              Path of a directory with images or a single image to process

optional arguments:
  -h, --help            show this help message and exit
  --dest_path {.}       Path of a directory where a result of the script will be saved
  --scale <1 - 500> {100}
                        Scale of the outputed text image
```