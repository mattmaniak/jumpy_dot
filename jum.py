#! /usr/bin/python3

from random import randint
from sys import exit as sys_exit
from termios import tcflush, TCIOFLUSH
from time import sleep
from select import select
from sys import stdin

import assets.gfx as gfx
import assets.window as window

frame_break = float(0.08) # Time to render a single frame.

# Frames, logic of rendering.
def frame():
	global frame_break

	random_delay = randint(0, 4) # Chance of 20% to speed up.
	window.enemy_x -= 1

	if window.idle(window.enemy_x) == 0: # Enemy behind the player.
		gfx.flush_previous_frame()

		if random_delay == 0 and frame_break > 0.04:
			frame_break -= 0.02 # Increase speed of the game.

		if frame_break == 0.08:
			window.score += 1

		elif frame_break == 0.06:
			window.score += 2

		else:
			window.score += 3

		window.enemy_x = randint(10, (gfx.x_size - window.player_x - 4))
		gfx.flush_previous_frame()
		window.idle_no_enemy()
		sleep(randint(0, 1))

def keypress(): # Keyboard-event.
	key, foo, bar = select([stdin], [], [], frame_break)
	if key: # key ('Enter' is the best way) is pressed: print with jump.
		return 1 # Any letter but empty and 'Enter' is enough.


while 1: # Main game loop.
	if keypress() == 1:
		tcflush(stdin, TCIOFLUSH) # Flush input buffer.

		for i in range(2): # Jump width. Must be smaller than player_x.
			gfx.flush_previous_frame()
			window.enemy_x -= 1 # Change enemy position.

			if window.jump(window.enemy_x) == 0: # Enemy behind the player.
				window.enemy_x = randint(10, (gfx.x_size - window.player_x - 4))

			sleep(frame_break)

	else:
		gfx.flush_previous_frame()
		frame()

