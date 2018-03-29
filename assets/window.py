from random import randint
from sys import exit as sys_exit

import assets.gfx as gfx

player_x = int(10) # Adjustable player position.
enemy_x = int(gfx.x - player_x - 4) # Enemy starting position.

def size_check():
	if gfx.x > 1024 or gfx.y > 1024:
		print("Window size error!")
		sys_exit()

	if gfx.x < player_x + 5 or gfx.y < 4:
		print("Window size error!")
		sys_exit()

# Non-playable area with clouds, above playable area.
def environment():
	gfx.horizontal_border()

	for i in range(gfx.y - 4): # Environment height.
		print(gfx.white + "#", end = "" + gfx.default) # Left border.

		for i in range(gfx.x - 2): # Spaces after left border.
			print(end = " ") # Environment empty area.

		print(gfx.white + "#" + gfx.default) # Right border.


# Area where Player takes activities with Enemies.
def jump(enemy_x):
	global player_x

	# Upper part of the playable_area.
	print(gfx.white + "#", end = "" + gfx.default) # Left border.

	for i in range(player_x): # Spaces after left border.
		print(end = " ")

	gfx.player()

	for i in range(gfx.x - player_x - 3): # Spaces before the left border.
		print(end = " ")

	print(gfx.white + "#" + gfx.default) # Right border.

	# Lower part of the playable_area.
	# Left, fixed border before the Player.
	print(gfx.white + "#", end = "" + gfx.default)

	for i in range(player_x + 1 + enemy_x):
		print(end = " ") # Spaces before the enemy, when the player jumps.

	gfx.enemy()

	for i in range(gfx.x - player_x - enemy_x - 4):
		print(end = " ") # Space chars after the Enemy.

	print(gfx.white + "#" + gfx.default) # Fixed border after the enemy.

	if enemy_x + player_x + 1 < 0: # 0 value makes 1 space between models.
		return 0


def idle(enemy_x):
	global player_x

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

	print(gfx.white + "#" + gfx.default) # Fixed border after the enemy.

	if enemy_x < 0: # 0 value makes 1 space between models.
		gfx.clearline()
		print(gfx.score + "Your score:" + gfx.default)
		sys_exit()

