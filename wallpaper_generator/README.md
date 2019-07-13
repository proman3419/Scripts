# Wallpaper generator

![alt text](https://github.com/proman3419/Scripts-and-tools/blob/master/wallpaper_generator/screenshot_1.png)

![alt text](https://github.com/proman3419/Scripts-and-tools/blob/master/wallpaper_generator/screenshot_2.png)

## Requirements
* Python 3.x
* Pillow 5.4.1

## Usage
You can use the script with a specific image or with a directory, in both cases you run the script the same way:

```python3 wallpaper_generator.py path```

The result of the script will be saved in the current working directory.

You can specify an outputed image's resolution like so:

```python3 wallpaper_generator.py path width height```

If width and height won't be specified the script will use resolution of a machine that it's run on.