from random import randint
from sys import exit as sys_exit

import assets.gfx as gfx

# Miscellaneous responsible for side things:
if gfx.x_size % 2 == 0: # Player centering.
	player_x = int(gfx.x_size / 2)

else:
	player_x = int((gfx.x_size + 1) / 2)

enemy_x = randint(10, (gfx.x_size - player_x - 2))
after_enemy_x = gfx.y_size - enemy_x
score = int(0)


# Main areas to render on the screen:
def environment(): # Non-playable area above the playable area.
	for i in range((gfx.y_size - 3) * gfx.x_size): # Render environment area.
		print(end = " ") # Environment empty area..

def empty(): # Upper part of the playable_area.
	for i in range(gfx.x_size):
		print(end = " ")

def render_player(): # Shows the player with specified position.
	for i in range(player_x): # Spaces before the player.
		print(end = " ")

	gfx.player()

def floor(): # Long block under the player and enemies.
	score_len = len(str(score))
	print(gfx.blue + " Score:", score, gfx.default, end = "")

	for i in range(gfx.x_size - score_len - 9):
		print(gfx.blue + "#" + gfx.default, end = "")



# Scenarios of rendering:
def jump(enemy_x): # Frame rendered when the player jumps.
	environment()
	render_player()
	for i in range(gfx.x_size - player_x - 1): # Spaces before the left border.
		print(end = " ")

	# Lower area:
	for i in range(player_x + enemy_x):
		print(end = " ") # Spaces before the enemy, when the player jumps.

	gfx.enemy()

	for i in range(gfx.x_size - player_x - enemy_x - 2):
		print(end = " ") # Space chars after the Enemy.

	print("") # Placeholder to put the keypress catcher to correct place.
	floor()

	if enemy_x + player_x < 0: # Enemy at the end of the map (left).
		return 0

def idle(enemy_x): # Scenario when there are no activities from the player.
	environment()
	empty()

	# Lower area:
	render_player()
	for i in range(enemy_x): # Spaces before the enemy.
		print(end = " ")

	gfx.enemy()

	for i in range(gfx.x_size - player_x - enemy_x - 2):
		print(end = " ") # Space chars after the Enemy.

	print("") # Placeholder to put the keypress catcher to correct place.
	floor()

	if enemy_x == 0: # If colission then end the game.
		score_len = len(str(score))
		gfx.clearline()
		print(gfx.blue + "Score:", score, gfx.default, end = "")

		for i in range(gfx.x_size - score_len - 17):
			print(gfx.blue + "#", end = "")

		print(gfx.red + "You lose!" + gfx.default)
		sys_exit()

	if enemy_x < 0:
		return 0

