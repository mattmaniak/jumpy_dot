import ui
from sys import exit

# Width and height must be entered manually and must be equal 1.
# Examples of models below.

# Some 'model' placeholders here.

def enemy():
	for i in range(1): # height
		print(ui.red + "#" + ui.default, end = "", flush = "True")

def player():
	for i in range(1): # height
		print(ui.green + "#" + ui.default, end = "", flush = "True")

