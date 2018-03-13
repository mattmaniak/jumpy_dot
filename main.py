#! /usr/bin/python3

import ui, models
from random import randint
from sys import stdout
from subprocess import call
from time import sleep

# import pdb

# You can set up height of user area to fit it.
playable_area_y = int(15)

# Non-playable area with clouds, above playable area.
def environment():
	ui.horizontal_border()

	for i in range(ui.y - playable_area_y - 3): # Environment height.
		# Positions of clouds.
		random_x = randint(0, ui.y - playable_area_y - 3)
		random_y = randint(0, ui.x - 2)

		print(ui.white + "#", end = "" + ui.default)

		# Whitespaces after left border.
		for i in range(ui.x - 2):
			print(ui.green + "#" + ui.default, end = "")

		# Right border:
		print(ui.white + "#" + ui.default)

# Area where Player takes activities with Enemies.
def playable_area():
	for i in range(playable_area_y - models.Player.height):

		# Left border.
		print(ui.white + "#", end = "" + ui.default)

		# Whitespaces after left border.
		for i in range(ui.x - 2):
			print("u", end = "")

		# Right border.
		print(ui.white + "#" + ui.default)
	
	# Left, fixed border before the Player.
	for i in range(models.Player.height):
		print(ui.white + "#", end = "" + ui.default)

	space_before_player = int(10)

	for i in range(space_before_player):
		print(ui.space, end = "")
	
	models.Player.model()
	
	# Space chars after the Player.
	for i in range(ui.x - models.Player.width - space_before_player - 2):
		print(ui.space, end = "")
	
	# Right, fixed border after the Player.
	for i in range(models.Player.height):
		print(ui.white + "#" + ui.default)
	
	ui.horizontal_border()

environment()
playable_area()

