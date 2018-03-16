#! /usr/bin/python3

import ui, models
from random import randint
from sys import stdout
from time import sleep

# You can set up height of the playable area to fit it.
# It must be set up manually in models.py file.
user_area_height = int(15)

# Non-playable area with clouds, above playable area.
def environment():
	ui.horizontal_border()

	for i in range(ui.y - user_area_height - 2): # Environment height.

		print(ui.white + "#", end = "" + ui.default)

		# Whitespaces after left border.
		for i in range(ui.x - 2):
			print(ui.bright_blue + "#" + ui.default, end = "")

# If you want check graphically environment height, replace above line with it.
			# print(ui.green + "#" + ui.default, end = "")

		# Right border:
		print(ui.white + "#" + ui.default)

# Area where Player takes activities with Enemies.
def playable_area():
	for i in range(user_area_height - 1): # models.Player.height

		# Left border.
		print(ui.white + "#", end = "" + ui.default)

		# Whitespaces after left border.
		for i in range(ui.x - 2):
			print(ui.space, end = "")

		# Right border.
		print(ui.white + "#" + ui.default)
	
	# Left, fixed border before the Player.
	for i in range(1): # models.Player.height
		print(ui.white + "#", end = "" + ui.default)

	# Define Player position
	player_x = int(10)

	for i in range(player_x):
		print(ui.space, end = "")
	
	models.player()

#	enemies_amount = randint(0, ui.x - player_x - models.Player.width - 2)

	enemies_amount = int(1)

	# 1 is player.width:
	enemy_x = randint(0, ui.x - 1 - player_x - enemies_amount - 2)

	# Space chars after the Player.
	for i in range(enemy_x):
		print(ui.space, end = "")

	for i in range(enemies_amount):
		models.enemy()

	# Space chars after the Enemy.

	# models.Player.width and models.Enemy.width are equal 1.
	for i in range(ui.x - player_x - enemy_x - 1 - 1 - 2):
		print(ui.space, end = "")
	
	# Right, fixed border after the Player.
	for i in range(1): # models.Player.height
		print(ui.white + "#" + ui.default)
	
	ui.horizontal_border()

# Example.
while True:
	environment()
	playable_area()
	sleep(1)

