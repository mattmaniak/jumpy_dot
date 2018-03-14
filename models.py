import ui
from sys import exit

# Width and height must be entered manually and must be equal 1.
# Examples of models below.

class Cloud:
	width = int(20)
	height = int(8)

	if width >= ui.x - 2:
		exit(ui.error + "Width must be less than ui.x - 2." + ui.default)

	if height >= ui.x - 18:
		exit("Height must be less than ui.x - 18.")

	def model():
		for i in range(Cloud.height):
			print(ui.white + "#", end = "" + ui.default)

			for i in range(Cloud.width):
				print(ui.white + "#" + ui.default)

class Enemy:
	width = int(1)
	height = int(1)

	if width >= ui.x - 2:
		exit(ui.error + "Width must be less than ui.x - 2." + ui.default)

	if height >= 15: # main.user_area_height
		exit("Width must be less than 'ui.user_area_height.'.")

	def model():
		for i in range(Enemy.height):
			print(ui.red + "#", end = "" + ui.default)

class Player:
	width = int(1)
	height = int(1)

	if width >= ui.x - 2:
		exit(ui.error + "Width must be less than ui.x - 2." + ui.default)

	if height >= 15: # main.user_area_height
		exit("Width must be less than ui.user_area_height.")

	def model():
		for i in range(Player.height):
			print(ui.green + "#", end = "" + ui.default)

