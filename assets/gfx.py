from os import popen
from sys import stdout

# Reads a terminal size based on chars.
y_size, x_size = popen("stty size", "r").read().split()
x_size = int(x_size)
y_size = int(y_size)

# ANSI escape codes. First three: normal text, color blocks on the bottom.
default = str("\033[0m")		# Terminal default text.
error = str("\033[41;30m")		# Black text with red background.
red = str("\033[31m")			# Color of enemies.
green = str("\033[92m")	# Colot of the player.
blue = str("\033[94m")	# Bright blue text.

white = str("\033[37m")			# Used for window debuggung.

def horizontal_border():
	for i in range(x):
		print(white + "#" + default, end = "")

def clearline():
	stdout.write("\033[F") # Back to the previous line.
	stdout.write("\033[K") # Clear the line.

# Models.
def enemy():
	print(red + "@" + default, end = "")

def player():
	print(green + "*" + default, end = "")

