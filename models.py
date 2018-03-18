import ui

# Size of models must be 1x1, eg. '#' - just one ASCII char.

def cloud():
	print(ui.white + "#" + ui.default, end = "", flush = "True")

def enemy():
	print(ui.red + "#" + ui.default, end = "", flush = "True")

def player():
	print(ui.green + "#" + ui.default, end = "", flush = "True")

