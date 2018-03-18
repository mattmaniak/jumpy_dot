#! /usr/bin/python3

from random import randint
from time import sleep

import assets.models as models
import assets.ui as ui
import assets.window as window

cloud_x = int(ui.x - 2)
player_x = int(0)
enemy_x = int(ui.x - player_x - 4)

def key_event():

	global cloud_x, enemy_x

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
	window.environment(cloud_x)
	window.playable_area(player_x, enemy_x)

	move = key_event()

	collision_check()

