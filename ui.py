from os import popen
from sys import stdout

# Reads a terminal size based on letters.
y, x = popen("stty size", "r").read().split()

x = int(x)
y = int(y)

space = str(" ")

# ANSI escape codes.
default = str("\033[0m")
error = str("\033[41;30m")

# Background and foreground are filled with the same color.
red = str("\033[41;31m")
green = str("\033[42;32m")
white = str("\033[47;37m")
bright_blue = str("\033[104;94m")

def horizontal_border():
	for i in range(x):
		print(white + "#" + default, end = "", flush = "True")

def clearline():
	stdout.write("\033[F") # Back to the previous line.
	stdout.write("\033[K") # Clear the line.

