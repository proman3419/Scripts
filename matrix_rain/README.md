# Matrix rain

![alt text](https://github.com/proman3419/Scripts-and-tools/blob/master/matrix_rain/screenshot.gif)

## Requirements
* Python 3.x
* keyboard 0.13.3

## Usage
**If you're running the script on Linux systems you'll have to grant it root privileges (they're required for the keyboard module). It's used for exitting the script.**

The script can be run like so:

```python3 matrix_rain.py```

In this case the default values of parameters will be used that is:

```
speed = 30     # speed of falling characters
min_cd = 0.1   # min consecutive chars
max_cd = 0.2   # max consecutive chars
min_sd = 0.3   # min consecutive spaces
max_sd = 0.4   # max consecutive spaces
```

The min and max values represent fractions of height of a terminal.

In order to use different values they need to be passed when invoking the script:

```python3 matrix_rain.py speed min_cd max_cd min_sd max_sd```

Here are ranges in which the arguments should be contained:

```
1 <= speed <= 100
0.05 <= min_cd <= 1
0.05 <= max_cd <= 1
0.05 <= min_sd <= 1
0.05 <= max_sd <= 1
```

To exit the script press BACKSPACE.
