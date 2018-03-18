#! /usr/bin/python3

from random import randint
from time import sleep

import ui, models, window

player_x = int(0)
enemy_x = int(ui.x - player_x - 4)

def key_event():

	global enemy_x

	sleep(0.1)
	key = str(input())
	ui.clearline()

	if key == "": # Empty input = 'Enter' key.
		enemy_x -= 1 # 0 value makes 1 space between models.
		return enemy_x

def collision_check():

	if enemy_x == -1:
		import sys
		ui.clearline
		sys.exit("You lose!")

while True:
	window.environment()
	window.playable_area(player_x, enemy_x)

	move = key_event()

	collision_check()

