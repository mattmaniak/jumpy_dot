#! /usr/bin/python3

from random import randint
from sys import exit as sys_exit
from termios import tcflush, TCIOFLUSH
from time import sleep
from select import select
from sys import stdin, stdout

import assets.gfx as gfx
import assets.window as window

frame_break = float(0.1) # Time to render single frame.
# It's also affects on the clouds and enemies speeds.

def rng():
	sleep(randint(0, 3)) # Enemy break pseudo-random generator.

def flush_previous_frame(): # Render the game in a single frame.
	for i in range(gfx.y - 1):
		gfx.clearline()
		stdout.flush()

def frame():
	global frame_break

	window.enemy_x -= 1
	window.environment()

	if window.idle(window.enemy_x) == 0:
		if frame_break > 0.05: # Maximum speed of the game.		
			frame_break -= 0.01

		window.score += 1
		window.score_check()
		window.enemy_x = int(gfx.x - window.player_x - 4)

		for i in range(2): # Remove above print (window.idle).
			gfx.clearline()

		window.idle_no_enemy()
		window.floor()
		rng()

def keypress():
	key, foo, bar = select([stdin], [], [], frame_break)

	if key: # key ('Enter' is the best way) is pressed: print with jump.
		return 1


window.winsize_check()

window.environment()	# \
window.idle_no_enemy()	# Initial frames.
window.floor()			# /

rng()					# Time stop before the game start.

flush_previous_frame()

window.environment()			# \
window.idle(window.enemy_x)		# Necessary to show the enemy at the end.
window.floor()					# /

while 1:
	if keypress() == 1:
		tcflush(stdin, TCIOFLUSH) # Flush input buffer.

		for i in range(1): # Jump width. Must be smaller than player_x.
			window.enemy_x -= 1

			flush_previous_frame()
			window.environment()

			if window.jump(window.enemy_x) == 0:
				window.enemy_x = int(gfx.x - window.player_x - 4)

			window.floor()
			sleep(frame_break)

	else:
		flush_previous_frame()
		frame()
		window.floor()

