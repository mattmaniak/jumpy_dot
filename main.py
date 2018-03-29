#! /usr/bin/python3

from random import randint
from sys import exit as sys_exit
from termios import tcflush, TCIOFLUSH
from time import sleep
from select import select
from sys import stdin

import assets.gfx as gfx
import assets.window as window

frame_break = float(0.1) # Time to render single frame.
# It's also affects on the clouds and enemies speeds.

def frame():
	window.enemy_x -= 1
	window.environment()
	window.idle(window.enemy_x)

def keypress():
	key, foo, bar = select([stdin], [], [], frame_break)

	if key: # key ('Enter' is the best way) is pressed: print with jump.
		return 1

	else: # If not clicked, print without jump.
		return 0

def round():
	if keypress() == 1:
		tcflush(stdin, TCIOFLUSH)

		for i in range(30): # Jump width.
			window.enemy_x -= 1
			window.environment()
			if window.jump(window.enemy_x) == 0:
				window.enemy_x = int(gfx.x - window.player_x - 4)

			sleep(frame_break)

		round()

	else:
		frame()
		round()

window.size_check()			# \
window.environment()		# Initial frames.
window.idle(window.enemy_x)	# /

round()

