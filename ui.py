from os import popen
from sys import exit, stdout

# Reads a terminal size based on letters.
y, x = popen("stty size", "r").read().split()

x = int(x)
y = int(y)

space = str(" ")

# ANSI escape codes.
default = "\033[0m"
error = "\033[41;30m"

# Background and foreground are filled with the same color.
red = "\033[41;31m"
green = "\033[42;32m"
blue = "\033[44;34m"
white = "\033[47;37m"

def horizontal_border():
	for i in range(x):
		print(white + "#", end = "" + default)

def clearline():
	stdout.write("\033[F") # Back to the previous line.
	stdout.write("\033[K") # Clear the line.

