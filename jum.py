#! /usr/bin/python3

from random import randint
from sys import exit as sys_exit
from termios import tcflush, TCIOFLUSH
from time import sleep
from select import select
from sys import stdin, stdout

import assets.gfx as gfx
import assets.window as window

frame_break = float(0.08) # Time to render a single frame.

# Frames, logic of rendering.
def frame(): # Frame
	global frame_break

	random_delay = randint(0, 4) # 20% of chance to speed up.
	window.enemy_x -= 1

	if window.idle(window.enemy_x) == 0: # Enemy behind the player.
		if random_delay == 0 and frame_break > 0.04:
			frame_break -= 0.02 # Increase speed of the game.

		flush_previous_frame()

		window.score += 1 # Python has got infinite number precision.
		window.enemy_x = int(gfx.x_size - window.player_x - 2)

		window.idle_no_enemy()
		sleep(randint(0, 1))

def flush_previous_frame(): # To render the game in a single frame.
	for i in range(gfx.y_size - 1):
		gfx.clearline()
		stdout.flush()

def keypress(): # Keyboard-event.
	key, foo, bar = select([stdin], [], [], frame_break)

	if key: # key ('Enter' is the best way) is pressed: print with jump.
		return 1 # Any letter but empty and 'Enter' is enough.


window.winsize_check()	# Check window size before start.
window.idle_no_enemy()	# Initial frame.
flush_previous_frame()
window.idle(window.enemy_x) # Frame necessary to show the enemy at the end.

while 1: # Main game loop.
	if keypress() == 1:
		tcflush(stdin, TCIOFLUSH) # Flush input buffer.

		for i in range(2): # Jump width. Must be smaller than player_x.
			flush_previous_frame()
			window.enemy_x -= 1 # Change enemy position.

			if window.jump(window.enemy_x) == 0: # Enemy behind the player.
				window.enemy_x = int(gfx.x_size - window.player_x - 2)

			sleep(frame_break)

	else:
		flush_previous_frame()
		frame()

