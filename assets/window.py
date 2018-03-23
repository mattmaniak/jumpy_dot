from random import randint

import assets.gfx as gfx


player_x = int(10) # Adjustable, fixed player position.

# Non-playable area with clouds, above playable area.
def environment():
	gfx.horizontal_border()

	for i in range(gfx.y - 4): # Environment height.
		print(gfx.white + "#", end = "" + gfx.default) # Left border.

		for i in range(gfx.x - 2): # Spaces after left border.
			print(end = " ") # Environment empty area.

		print(gfx.white + "#" + gfx.default) # Right border.


# Area where Player takes activities with Enemies.
def jump():
	# Upper part of the playable_area.
	print(gfx.white + "#", end = "" + gfx.default) # Left border.

	for i in range(gfx.x - 2): # Spaces after left border.
		print(end = " ")

	print(gfx.white + "#" + gfx.default) # Right border.


def idle(enemy_x):
	global player_x

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

	print(gfx.white + "#" + gfx.default) # Fixed border after the enemy.

