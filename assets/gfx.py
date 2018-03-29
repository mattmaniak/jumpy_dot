from os import popen
from sys import stdout

# Reads a terminal size based on chars.
y, x = popen("stty size", "r").read().split()
x = int(x)
y = int(y)

# ANSI escape codes. First three: normal text, color blocks on the bottom.
default = str("\033[0m") # Terminal default text.
error = str("\033[41;30m") # Black text with red background.
green = str("\033[32m") # Green text.
bright_blue = str("\033[94m")

# Blocks
red_b = str("\033[41;31m")
green_b = str("\033[42;32m")
white_b = str("\033[47;37m")
bright_blue_b = str("\033[104;94m")

def horizontal_border():
	for i in range(x):
		print(white + "#" + default, end = "")

def input_border():
	for i in range(x - 1):
		print(white + "#" + default, end = "")

def clearline():
	stdout.write("\033[F") # Back to the previous line.
	stdout.write("\033[K") # Clear the line.

def enemy(): # Models.
	print(red_b + "#" + default, end = "")

def player():
	print(green_b + "#" + default, end = "")

