from random import randint
from sys import exit as sys_exit
from time import sleep

import assets.gfx as gfx

# Miscellaneous responsible for side things.
if gfx.x_size % 2 == 0: # Player centering.
	player_x = int(gfx.x_size / 2)
else:
	player_x = int((gfx.x_size + 1) / 2)

enemy_x = int(gfx.x_size - player_x - 4) # Enemy starting position.
score = int(0)

def winsize_check(): # Check window size.
	if gfx.x_size > 320 or gfx.y_size > 128:
		print(gfx.error + "Screen to big! Game experience might be low!"
		+ gfx.default)

		sys_exit()

	if gfx.x_size < player_x + 5 or gfx.y_size < 4:
		print(gfx.error + "Window to small error!" + gfx.default)
		sys_exit()


# Main areas to render on the screen.
def environment(): # Non-playable area above the playable area.
	for i in range(gfx.x_size):
		print(gfx.white + "#" + gfx.default, end = "")

	for i in range(gfx.y_size - 5): # Environment height.
		print(gfx.white + "#" + gfx.default, end = "") # Left border.

		for i in range(gfx.x_size - 2): # Spaces after left border.
			print(end = " ") # Environment empty area.

		print(gfx.white + "#" + gfx.default) # Right border.

def floor(): # Long block under the player and enemies.
	score_len = len(str(score))

	print(gfx.blue + "Score:", score, gfx.default, end = "")

	for i in range(gfx.x_size - score_len - 9):
		print(gfx.blue + "#", end = "")

	print("#" + gfx.default)

def jump(enemy_x): # Frame rendered when the player jumps.
	# Upper part of the playable_area.
	print(gfx.white + "#" + gfx.default, end = "") # Left border.

	for i in range(player_x): # Spaces after left border.
		print(end = " ")

	gfx.player()

	for i in range(gfx.x_size - player_x - 3): # Spaces before the left border.
		print(end = " ")

	print(gfx.white + "#" + gfx.default) # Right border.

	# Lower part of the playable_area.
	# Left, fixed border before the Player.
	print(gfx.white + "#" + gfx.default, end = "")

	for i in range(player_x + 1 + enemy_x):
		print(end = " ") # Spaces before the enemy, when the player jumps.

	gfx.enemy()

	for i in range(gfx.x_size - player_x - enemy_x - 4):
		print(end = " ") # Space chars after the Enemy.

	print(gfx.white + "#" + gfx.default) # Border after the enemy.

	floor()

	if enemy_x + player_x < 0: # Enemy at the end of the map (left).
		return 0

def idle(enemy_x): # Scenario when there are no activities from the player.
	# Upper part of the playable_area.
	print(gfx.white + "#" + gfx.default, end = "") # Left border.

	for i in range(gfx.x_size - 2): # Spaces after left border.
		print(end = " ")

	print(gfx.white + "#" + gfx.default) # Right border.

	# Lower part of the playable_area.
	# Left, fixed border before the Player.
	print(gfx.white + "#" + gfx.default, end = "")

	for i in range(player_x): # Spaces before the player.
		print(end = " ")

	gfx.player()

	for i in range(enemy_x): # Spaces before the enemy.
		print(end = " ")

	gfx.enemy()

	for i in range(gfx.x_size - player_x - enemy_x - 4):
		print(end = " ") # Space chars after the Enemy.

	print(gfx.white + "#" + gfx.default) # Border after the enemy.

	floor()

	if enemy_x == 0: # If colission then end the game.
		score_len = len(str(score))

		gfx.clearline()

		print(gfx.blue + "Score:", score, gfx.default, end = "")

		for i in range(gfx.x_size - score_len - 17):
			print(gfx.blue + "#", end = "")

		print(gfx.red + "You lose!" + gfx.default)
		sleep(3)
		sys_exit()

	if enemy_x < 0:
		return 0

def idle_no_enemy():	# Rendered like above but without enemy.
	# Upper part of the playable_area.
	print(gfx.white + "#" + gfx.default, end = "") # Left border.

	for i in range(gfx.x_size - 2): # Spaces after left border.
		print(end = " ")

	print(gfx.white + "#" + gfx.default) # Right border.

	# Lower part of the playable_area.
	# Left, fixed border before the Player.
	print(gfx.white + "#" + gfx.default, end = "")

	for i in range(player_x): # Spaces before the player.
		print(end = " ")

	gfx.player()

	for i in range(enemy_x + 1): # Spaces before the enemy.
		print(end = " ")

	print(gfx.white + "#" + gfx.default) # Border after the enemy.

	floor()

# Any other functions.
def score_check():	# Score checker to provide a glory of the integer.
	if score >= 0x7fffffff: # 2147483647
		gfx.clearline()

		print(gfx.error
			+ "Python supports bignums but God save the int!",
			score, gfx.default)

		sys_exit()

