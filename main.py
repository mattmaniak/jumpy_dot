#! /usr/bin/python3

import ui, models

from random import randint
from sys import stdout
from subprocess import call
from time import sleep

# Non-playable area with clouds, above playable area.
def environment():
	ui.horizontal_border()

	for i in range(ui.y - 18): # Environment height.

		random_x = randint(0, ui.y - 18)
		random_y = randint(0, ui.x - 2)

		print(ui.white + "#", end = "" + ui.default)

		# Whitespaces after left border.
		for i in range(ui.x - 2):
			print("s", end = "")

		# Right border:
		print(ui.white + "#" + ui.default)

environment()

# Gaming area:
for i in range(15):
	print(ui.white + "#", end = "" + ui.default)

	# Whitespaces after left border.
	for i in range(ui.x - 2):
		print(ui.space, end = "")

	# Right border:
	print(ui.white + "#" + ui.default)

ui.horizontal_border()
