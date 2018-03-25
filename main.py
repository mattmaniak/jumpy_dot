#! /usr/bin/python3

from random import randint
from sys import exit as sys__exit
from time import sleep
from select import select
from sys import stdin

import assets.gfx as gfx
import assets.window as window

enemy_x = int(gfx.x - window.player_x - 4) # Enemy starting position.

frame_break = float(0.5) # Time to render single frame.
# It's also affects on the clouds and enemies speeds.

def key_event():
	key, foo, bar = select([stdin], [], [], 1) # After key, moves faster.

def enemy_move():
	global enemy_x

	while 1:
		sleep(frame_break)
		enemy_x -= 1
		return enemy_x

def collision_check():
	if enemy_x < 0: # 0 value makes 1 space between models.
		gfx.clearline()
		print(gfx.score + "Your score:" + gfx.default)
		sys__exit()


window.environment()
window.idle(enemy_x)


while 1: # Test.
	enemy_move()

	key_event()

	window.environment()
	window.jump(enemy_x)

