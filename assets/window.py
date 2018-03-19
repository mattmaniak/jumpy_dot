from random import randint

import assets.gfx as gfx

# Non-playable area with clouds, above playable area.
def environment(cloud_x):
	gfx.horizontal_border()

	for i in range(gfx.y - 4): # Environment height.
		print(gfx.white + "#", end = "" + gfx.default) # Left border.

		for i in range(gfx.x - 2): # Spaces after left border.
			print(end = " ") # Environment empty area.

		print(gfx.white + "#" + gfx.default) # Right border.


# Area where Player takes activities with Enemies.
def playable_area(player_x, enemy_x):
#	player_x = int(0) # Define Player position.

	# Amount of spaces between the player and the enemy.
#	enemy_x = randint(0, gfx.x - player_x - 4)


	# Upper part of the playable_area.
	print(gfx.white + "#", end = "" + gfx.default) # Left border.

	for i in range(gfx.x - 2): # Spaces after left border.
		print(end = " ")

	print(gfx.white + "#" + gfx.default) # Right border.


	# Lower part of the playable_area.
	# Left, fixed border before the Player.
	print(gfx.white + "#", end = "" + gfx.default)

	for i in range(player_x): # Spaces before the player.
		print(end = " ")
	
	gfx.player()

	for i in range(enemy_x): # Space chars after the player.
		print(end = " ")

	gfx.enemy()

	for i in range(gfx.x - player_x - enemy_x - 4):
		print(end = " ") # Space chars after the Enemy.
	
	print(gfx.white + "#" + gfx.default) # Fixed border after the player.
	
#	gfx.horizontal_border()

