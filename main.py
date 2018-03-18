#! /usr/bin/python3

from time import sleep

import ui, models, window

def key_event():
	key = str(input("Enter: "))

	if key == "":
		return 1

move = key_event()

window.environment()
window.playable_area(move)

