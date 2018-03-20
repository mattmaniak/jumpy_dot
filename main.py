#! /usr/bin/python3

from random import randint
from sys import exit as sys_exit
from time import sleep

import assets.gfx as gfx
import assets.window as window

player_x = int(10)
enemy_x = int(gfx.x - player_x - 4)

time_score = int(0)

frame_break = float(0.1) # Time to render single frame.
# It's also affects on the clouds and enemies speeds.


# def key_event():
#	global cloud_x, enemy_x

#	sleep(frame_break)
#	key = str(input())
#	gfx.clearline()

#	if key == "": # Empty input = 'Enter' key.
#		enemy_x -= 1
#		return enemy_x

def enemy_move():
	global enemy_x

	while 1:
		sleep(frame_break)
		enemy_x -= 1
		return enemy_x

def collision_check():
	if enemy_x < 0: # 0 value makes 1 space between models.
		gfx.clearline()
		print(gfx.score + "Your score:", time_score, "s." + gfx.default)
		sys_exit()

def cloud_move():
	global cloud_x

	while 1:
		sleep(frame_break)
		cloud_x -= 1

		if cloud_x == 0:
			cloud_x = gfx.x - 3 # It won't work with cloux_x != 1.

		return cloud_x


while 1: # Test.
	window.environment()
	window.playable_area(player_x, enemy_x)

	enemy_move()

	collision_check()

