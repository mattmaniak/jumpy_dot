#! /usr/bin/python3

from random import randint
from sys import exit as sys_exit
from termios import tcflush, TCIOFLUSH
from time import sleep
from select import select
from sys import stdin

import assets.gfx as gfx
import assets.window as window

enemy_break = randint(0, 3)
frame_break = float(0.05) # Time to render single frame.
# It's also affects on the clouds and enemies speeds.

def frame():
	window.enemy_x -= 1
	window.environment()

	if window.idle(window.enemy_x) == 0:
		window.enemy_x = int(gfx.x - window.player_x - 4)
		

def keypress():
	key, foo, bar = select([stdin], [], [], frame_break)

	if key: # key ('Enter' is the best way) is pressed: print with jump.
		return 1

def main(): # Also game logic.
	if keypress() == 1:
		tcflush(stdin, TCIOFLUSH) # Flush input buffer.

		for i in range(5): # Jump width.
			window.enemy_x -= 1
			window.environment()

			if window.jump(window.enemy_x) == 0:
				window.enemy_x = int(gfx.x - window.player_x - 4)
				window.score += 1
				window.score_check()

			sleep(frame_break)

		main()

	else:
		frame()
		main()

window.winsize_check()		# \
window.environment()		# Initial frames.
window.idle(window.enemy_x)	# /
sleep(enemy_break)

main()

