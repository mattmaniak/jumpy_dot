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

window.size_check()
window.environment() # Initial frames.
window.idle(window.enemy_x)

def jump_frame():
	for i in range(10): # Jump width.
		window.enemy_x -= 1
		window.environment()
		window.jump(window.enemy_x)
		sleep(frame_break)

def key_event():
	key, foo, bar = select([stdin], [], [], frame_break)

	if key: # key ('Enter' is the best way) is pressed: print with jump.
		return 1

	else: # If not clicked, print without jump.
		return 0

def round():
	if key_event() == 1:
		jump_frame()
		tcflush(stdin, TCIOFLUSH)
		round()

	else:
		frame()
		round()

round()

