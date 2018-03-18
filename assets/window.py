from random import randint

import assets.models as models
import assets.ui as ui

# Non-playable area with clouds, above playable area.
def environment(cloud_x):

	ui.horizontal_border()

	for i in range(ui.y - 4): # Environment height.
		print(ui.white + "#", end = "" + ui.default) # Left border.

		for i in range(ui.x - 2): # Spaces after left border.
			print(ui.bright_blue + "#" + ui.default, end = "")

		print(ui.white + "#" + ui.default) # Right border.


# Area where Player takes activities with Enemies.
def playable_area(player_x, enemy_x):

#	player_x = int(0) # Define Player position.

	# Amount of spaces between the player and the enemy.
#	enemy_x = randint(0, ui.x - player_x - 4)


	# Upper part of the playable_area.
	print(ui.white + "#", end = "" + ui.default) # Left border.

	for i in range(ui.x - 2): # Spaces after left border.
		print(ui.space, end = "")

	print(ui.white + "#" + ui.default) # Right border.


	# Lower part of the playable_area.
	# Left, fixed border before the Player.
	print(ui.white + "#", end = "" + ui.default)

	for i in range(player_x): # Spaces before the player.
		print(ui.space, end = "")
	
	models.player()

	for i in range(enemy_x): # Space chars after the player.
		print(ui.space, end = "")

	models.enemy()

	for i in range(ui.x - player_x - enemy_x - 4):
		print(ui.space, end = "") # Space chars after the Enemy.
	
	print(ui.white + "#" + ui.default) # Fixed border after the player.
	
#	ui.horizontal_border()

