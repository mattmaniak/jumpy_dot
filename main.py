#! /usr/bin/python3

from random import randint
from sys import exit as sys__exit
from time import sleep
from select import select
from sys import stdin

import assets.gfx as gfx
import assets.window as window

frame_break = float(0.1) # Time to render single frame.
# It's also affects on the clouds and enemies speeds.

def key_event():
	global enemy_x

	key, foo, bar = select([stdin], [], [], frame_break) # After key, moves faster.

#	key = str(input()) # Pseudo key event.

	if key: # 'Enter' key simulation. Print with jump.
		window.enemy_x -= 1
		window.environment()
		window.jump(window.enemy_x)
		sleep(frame_break)

	else: # If not enter, print without jump.	
		window.enemy_x -= 1
		window.environment()
		window.idle(window.enemy_x)
		sleep(frame_break)

def enemy_move():
	global enemy_x

	while 1:
		sleep(frame_break)
		
		return window.enemy_x

def collision_check():
	if enemy_x < 0: # 0 value makes 1 space between models.
		gfx.clearline()
		print(gfx.score + "Your score:" + gfx.default)
		sys__exit()


window.environment()
window.idle(window.enemy_x)


while 1: # Test.
	key_event()

