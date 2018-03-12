#! /usr/bin/python3

import ui, models

from random import randint
from sys import stdout
from subprocess import call
from time import sleep

def player_render():
	ui.horizontal_border()

	# Left, vertical border:
	print(ui.white_block + "#", end = "" + ui.default)

	position = int(float(0.5 * ui.x - 0.5 * models.Player.width))

	# Space after left border:
	print(position * ui.space, end = "")

	models.Player.model()

	# Space before fixed, left border:
	for i in range(ui.x - position - models.Player.width - 2):
		print(ui.space, end = "")

	# Right, vertical border:
	print(ui.white_block + "#" + ui.default)

def enem_render():
	# Window height:
	for i in range(ui.y - 3):
		print(ui.white_block + "#", end = "" + ui.default)

		# Random amount of spaces before the Enemy:
		random_x = randint(models.Enemies.width, ui.x - 2)

		# Whitespaces after left border.
		for i in range(models.Enemies.width, random_x):
			print(ui.space, end = "")

		models.Enemies.model()

		# Before right border:
		for i in range(ui.x - random_x - 2):
			print(ui.space, end = "")

		# Right border:
		print(ui.white_block + "#" + ui.default)

player_render()
enem_render()

