import os
import sys

# Reads a terminal size based on chars.
x_size, y_size = os.get_terminal_size()
x_size = int(x_size)
y_size = int(y_size)

if x_size < 40 or y_size < 5:
    print("To small window!")
    exit(1)


# ANSI escape codes. First three: normal text, color blocks on the bottom.
default = str("\033[0m")  # Terminal default text.
red = str("\033[31m")  # Color of enemies.
green = str("\033[92m")  # Colot of the player.
blue = str("\033[94m")  # Bright blue (floor).


def horizontal_border():
    global x_size
    global white

    for i in range(x_size):
        print('#' + default, end='')


def clearline():
    sys.stdout.write("\033[F\033[K")  # Back to the previous line and clear.


def flush_previous_frame():  # To render the game in a single frame.
    for i in range(y_size):
        clearline()
        sys.stdout.flush()


# Models:
def enemy():
    print(red + '@' + default, end='')


def player():
    print(green + '*' + default, end='')
