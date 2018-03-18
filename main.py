#! /usr/bin/python3

from time import sleep

import ui, models, window

position = int(0)

def key_event():
	global position

	key = str(input("Enter: "))

	

	if key == "":
		position += 1
		return position

while True:
	move = key_event()

	window.environment()
	window.playable_area(move)

