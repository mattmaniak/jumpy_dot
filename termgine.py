#! /usr/bin/python3

from os import popen
from random import randint
from sys import exit, stdout
from time import sleep

import pdb

class UI:
# ANSI escape codes. Background and foreground are filled with the same color.
	reset = "\033[0m"
	red_red = "\033[41;31m"
	green_green = "\033[42;32m"
	white_white = "\033[47;37m"

	y, x = popen("stty size", "r").read().split()
	x = int(x)
	y = int(y)

	space = str(" ")

	def horizontal_border():
		for i in range(UI.x):
			print(UI.white_white + "#", end = "" + UI.reset)

	def clearline():
		stdout.write("\033[F") # Back to previous line.
		stdout.write("\033[K") # Clearline.

class Player:
	width = int(5)
	if width >= UI.x - 2:
		exit("Width must be less than UI.x - 2!")

	def model():
		print(UI.green_green + Player.width * "@", end = "" + UI.reset)

	def render():
		UI.horizontal_border()
		print(UI.white_white + "#", end = "" + UI.reset) # Left, vertical border.

		position = int(float(0.5 * UI.x - 0.5 * Player.width))

		print(position * UI.space, end = "") # Space after left border.

		Player.model()

		for i in range(UI.x - position - Player.width - 2):
			print(UI.space, end = "") # Space before fixed, left border.

		print(UI.white_white + "#" + UI.reset) # Right, vertical border.

class Enemies:
	width = int(10)
	if width >= UI.x - 2:
		exit("Width must be less than UI.x - 2!")

	def model():
		print(UI.red_red + Enemies.width * "$", end = "" + UI.reset)

	def render():
# Rendering empty space.
		for i in range(UI.y - 3):
			print(UI.white_white + "#" + UI.reset, end = "")

			for i in range(UI.x - 2):
				print(UI.space, end = "")

			print(UI.white_white + "#" + UI.reset)

			UI.clearline()

# Rendering Enemies:
		for i in range(UI.y - 3): # Window height.
			print(UI.white_white + "#", end = "" + UI.reset) # Left border.

			# Random amount of spaces before the Enemy:
			random_x = randint(Enemies.width, UI.x - 2)

			for i in range(Enemies.width, random_x): # After left border.
				print(UI.space, end = "")

			Enemies.model()

			for i in range(UI.x - random_x - 2): # Before right border.
				print(UI.space, end = "")

			print(UI.white_white + "#" + UI.reset) # Right border.

#			UI.clearline()

Player.render()
Enemies.render()

