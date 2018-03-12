#! /usr/bin/python3

import ui

from sys import exit

# Width and height must be entered manually!

class Cloud:
	width = int(20)
	height = int(8)

	if width >= ui.x - 2:
		exit(ui.error + "Width must be less than ui.x - 2." + ui.default)

	if height >= ui.x - 18:
		exit("Height must be less than ui.x - 18.")

	def model():
		print(ui.blue + Cloud.width * "#")
		print(ui.blue + Cloud.width * "#")
		print(ui.blue + Cloud.width * "#")
		print(ui.blue + Cloud.width * "#")
		print(ui.blue + Cloud.width * "#")
		print(ui.blue + Cloud.width * "#")
		print(ui.blue + Cloud.width * "#")
		print(ui.blue + Cloud.width * "#")
		print(ui.blue + Cloud.width * "#" + ui.default)

class Enemy:
	width = int(10)
	height = int(1)

	if width >= ui.x - 2:
		exit(ui.error + "Width must be less than ui.x - 2." + ui.default)

	if height >= 15:
		exit("Width must be less than 15.")

	def model():
		print(ui.red_block + Enemies.width * "#", end = "" + ui.default)

class Player:
	width = int(5)
	height = int(1)

	if width >= ui.x - 2:
		exit(ui.error + "Width must be less than ui.x - 2." + ui.default)

	if height >= 15:
		exit("Width must be less than 15.")

	def model():
		print(ui.green_block + Player.width * "#", end = "" + ui.default)

