from random import randint

import assets.gfx as gfx

# Non-playable area with clouds, above playable area.
def environment(cloud_x):
	gfx.horizontal_border()

	for i in range(3): # Environment height.
		print(gfx.white + "#", end = "" + gfx.default) # Left border.

		for i in range(gfx.x - 2): # Spaces after left border.
			print(end = " ") # Environment empty area.

		print(gfx.white + "#" + gfx.default) # Right border.


	print(gfx.white + "#" + gfx.default, end = "")

	for i in range(cloud_x):
		print(end = " ")

	gfx.cloud()

	for i in range(gfx.x - cloud_x - 3): # 1 is the cloud width.
		print(end = " ")

	print(gfx.white + "#" + gfx.default)


	for i in range(gfx.y - 8): # Environment height.
		print(gfx.white + "#", end = "" + gfx.default) # Left border.

		for i in range(gfx.x - 2): # Spaces after left border.
			print(end = " ") # Environment empty area.

		print(gfx.white + "#" + gfx.default) # Right border.


# Area where Player takes activities with Enemies.
def playable_area(player_x, enemy_x):
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

