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

def round():
	global enemy_x

	key, foo, bar = select([stdin], [], [], frame_break) # Key event.

	if key: # key ('Enter' is the best way) is pressed: print with jump.
		for i in range(3):
			window.enemy_x -= 1
			window.environment()
			window.jump(window.enemy_x)
			sleep(2 * frame_break) # 0.2 seconds.

		else:
			window.enemy_x -= 1
			window.environment()
			window.idle(window.enemy_x)
			sleep(frame_break)

	else: # If not clicked, print without jump.
		window.enemy_x -= 1
		window.environment()
		window.idle(window.enemy_x)
		sleep(frame_break)

window.environment() # Initial frames.
window.idle(window.enemy_x)

while 1:
	round()

