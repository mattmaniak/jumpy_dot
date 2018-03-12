#! /usr/bin/python3

import ui

from sys import exit

class Player:
	width = int(5)
	height = int(1)

	if width >= ui.x - 2:
		exit("Width must be less than ui.x - 2!")

	def model():
		print(ui.green_block + Player.width * "#", end = "" + ui.default)

class Enemies:
	width = int(10)
	height = int(1)

	if width >= ui.x - 2:
		exit("Width must be less than ui.x - 2!")

	def model():
		print(ui.red_block + Enemies.width * "#", end = "" + ui.default)

