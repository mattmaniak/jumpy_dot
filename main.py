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

	key, foo, bar = select([stdin], [], [], frame_break)

	if key: # 'Enter' key simulation. Print with jump.
		window.enemy_x -= 1
		window.environment()
		window.jump(window.enemy_x)
		sleep(2 * frame_break) # 0.2 seconds.

	else: # If not enter, print without jump.	
		window.enemy_x -= 1
		window.environment()
		window.idle(window.enemy_x)
		sleep(frame_break)

window.environment()
window.idle(window.enemy_x)

while 1: # Test.
	key_event()

