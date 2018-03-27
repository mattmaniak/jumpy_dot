#! /usr/bin/python3

from random import randint
from sys import exit as sys_exit
from time import sleep
from select import select
from sys import stdin

import assets.gfx as gfx
import assets.window as window

frame_break = float(0.05) # Time to render single frame.
# It's also affects on the clouds and enemies speeds.

def frame():
	window.enemy_x -= 1
	window.environment()
	window.idle(window.enemy_x)

window.size_check()
window.environment() # Initial frames.
window.idle(window.enemy_x)


while 1:
	key, foo, bar = select([stdin], [], [], frame_break) # Key event.

	if key: # key ('Enter' is the best way) is pressed: print with jump.
		for i in range(10): # Jump width.
			window.enemy_x -= 1
			window.environment()
			window.jump(window.enemy_x)
			sleep(frame_break)

		while 1:
			frame()
			sleep(frame_break)

	else: # If not clicked, print without jump.
		frame()

