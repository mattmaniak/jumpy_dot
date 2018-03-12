#! /usr/bin/python3

from os import popen
from sys import exit, stdout

# ANSI escape codes.
# Background and foreground are filled with the same color.

default = "\033[0m"
red_block = "\033[41;31m"
green_block = "\033[42;32m"
white_block = "\033[47;37m"

# Reads a terminal size based on letters.
y, x = popen("stty size", "r").read().split()
x = int(x)
y = int(y)

space = str(" ")

def horizontal_border():
	for i in range(x):
		print(white_block + "#", end = "" + default)

def clearline():
	stdout.write("\033[F") # Back to the previous line.
	stdout.write("\033[K") # Clear the line.

