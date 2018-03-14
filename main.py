#! /usr/bin/python3

import ui, models
from random import randint
from sys import stdout
from subprocess import call
from time import sleep

# You can set up height of the playable area to fit it.
user_area_height = int(15)

# Non-playable area with clouds, above playable area.
def environment():
	ui.horizontal_border()

	for i in range(ui.y - user_area_height - 3): # Environment height.
		# Positions of clouds.
		random_x = randint(0, ui.y - user_area_height - 3)
		random_y = randint(0, ui.x - 2)

		print(ui.white + "#", end = "" + ui.default)

		# Whitespaces after left border.
		for i in range(ui.x - 2):
			print(ui.green + "#" + ui.default, end = "")

		# Right border:
		print(ui.white + "#" + ui.default)

# Area where Player takes activities with Enemies.
def playable_area():
	for i in range(user_area_height - models.Player.height):

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

	# Define Player position
	player_x = int(10)

	for i in range(player_x):
		print(ui.space, end = "")
	
	models.Player.model()

#	enemies_amount = randint(0, ui.x - player_x - models.Player.width - 2)

	enemies_amount = int(1)
	enemy_x = randint(0, ui.x - models.Player.width - player_x - enemies_amount - 2)

	# Space chars after the Player.
	for i in range(enemy_x):
		print(ui.space, end = "")

	for i in range(enemies_amount):
		models.Enemy.model()

	# Temponary space chars after the Enemy.
	for i in range(ui.x - player_x - enemy_x - models.Player.width - models.Enemy.width - 2):
		print(ui.space, end = "")
	
	# Right, fixed border after the Player.
	for i in range(models.Player.height):
		print(ui.white + "#" + ui.default)
	
	ui.horizontal_border()

environment()
playable_area()

while True:
	key = str(input("Type: "))

	if key == "":
		print(end = "")

	else:
		print("Press enter to steer!")

