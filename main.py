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
	sleep(frame_break)

def logic(state):
	global enemy_x

	key, foo, bar = select([stdin], [], [], frame_break) # Key event.

	if key: # key ('Enter' is the best way) is pressed: print with jump.
		return "jump"

#		else:
#			frame()

	else: # If not clicked, print without jump.
		return "idle"

window.size_check()
window.environment() # Initial frames.
window.idle(window.enemy_x)

state = str("")

while 1:
	if logic(state) == "jump":
		for i in range(3):
			window.enemy_x -= 1
			window.environment()
			window.jump(window.enemy_x)
			sleep(2 * frame_break)

		while 1:
			frame()

	elif logic(state) == "idle":
		frame()

