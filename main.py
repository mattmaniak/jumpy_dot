#! /usr/bin/python3

from time import sleep

import ui, models, window

def key_event():
	key = str(input("Enter: "))

	if key == "":
		print("ok")


window.environment()
window.playable_area()

