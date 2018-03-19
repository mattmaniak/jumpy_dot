#! /usr/bin/python3

from random import randint
from sys import exit as sys_exit
from time import sleep

import assets.gfx as gfx
import assets.window as window

cloud_x = int(gfx.x - 2) # - 2 due the temponary, vertical borders.
player_x = int(10)
enemy_x = int(gfx.x - player_x - 4)

time = int(0)

def key_event():
	global cloud_x, enemy_x

	sleep(0.1)
	key = str(input())
	gfx.clearline()

	if key == "": # Empty input = 'Enter' key.
		enemy_x -= 1
		return enemy_x

def enemy_move():
	global cloud_x, enemy_x

	while 1:
		sleep(0.1)
		enemy_x -= 4
		return enemy_x

def collision_check():
	if enemy_x < 0: # 0 value makes 1 space between models.
		gfx.clearline()
		print(gfx.score + "Your score:", time, "s." + gfx.default)
		sys_exit()

while 1: # Test.
	window.environment(cloud_x)
	window.playable_area(player_x, enemy_x)

	move = enemy_move()

	collision_check()

