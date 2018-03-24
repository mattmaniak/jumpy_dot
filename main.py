#! /usr/bin/python3

from random import randint
from sys import exit as sys__exit
from time import sleep

import assets.gfx as gfx
import assets.window as window

from sys import stdin
from threading import Thread
from subprocess import call
import signal

enemy_x = int(gfx.x - window.player_x - 4) # Enemy starting position.

frame_break = float(0.1) # Time to render single frame.
# It's also affects on the clouds and enemies speeds.

def key_event():
	global enemy_x

	key = None

	def time_pass():
		sleep(frame_break - 0.01)
		if key != None:
			return 0

		window.environment()
		window.jump()
		window.idle(enemy_x)

	Thread(target = time_pass).start()
	key = str(input())

#	if key == "": # Empty input = 'Enter' key event.
#		window.environment()
#		window.jump()
#		window.idle(enemy_x)

def enemy_move():
	global enemy_x

	while 1:
		sleep(frame_break)
		enemy_x -= 1
		return enemy_x

def collision_check():
	if enemy_x < 0: # 0 value makes 1 space between models.
		gfx.clearline()
		print(gfx.score + "Your score:" + gfx.default)
		sys__exit()


window.environment()	# \
window.jump()			# Game start positions.
window.idle(enemy_x)	# /

while 1: # Test.
	enemy_move()

	key_event()

	collision_check()

	window.environment()
	window.jump()
	window.idle(enemy_x)

