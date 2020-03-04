# Matrix rain

![alt text](https://github.com/proman3419/Scripts-and-tools/blob/master/matrix_rain/screenshot.gif)

## Usage
```
usage: matrix_rain.py [-h] [--speed <1 - 100> {25}]
                      [--min_cd <0.01 - 1.0> {0.1}]
                      [--max_cd <0.01 - 1.0> {0.2}]
                      [--min_sd <0.01 - 1.0> {0.3}]
                      [--max_sd <0.01 - 1.0> {0.4}]

In order to exit the script press BACKSPACE.
The script should be run as root in order to capture a BACKSPACE press.
Next to arguments names there is info about: <range> {default value}.

Will you pick the red pill or the blue pill?

optional arguments:
  -h, --help            show this help message and exit
  --speed <1 - 100> {25}
                        Speed of falling characters
  --min_cd <0.01 - 1.0> {0.1}
                        Min consecutive characters (part of screen height)
  --max_cd <0.01 - 1.0> {0.2}
                        Max consecutive characters (part of screen height)
  --min_sd <0.01 - 1.0> {0.3}
                        Min consecutive spaces (part of screen height)
  --max_sd <0.01 - 1.0> {0.4}
                        Max consecutive spaces (part of screen height)
```