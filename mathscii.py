#s/o polyhurt for the idea
from math import *
import os
import time
fg_range = range(30, 38)
bg_range = range(40, 48)
fg_offset = 30
bg_offset = 40
def colorPrint(fg, bg, txt):
	print("\x1b["+";".join(["3", str(fg), str(bg)])+"m"+txt+"\x1b[0m", end="")
def getBlankCanvas(fill, size_x, size_y):
	canvas = []
	for y in range(0, size_y):
		canvas.append([])
		for x in range(0, size_x):
			canvas[y].append(fill)
			#canvas[y][x] = fill
	return canvas
def printCanvas(canvas):
	for y in canvas:
		for x in y:
			colorPrint(str(fg_offset + x), str(bg_offset + x), "#")
		cp = y
		cp.reverse()
#		for x in cp:
#			colorPrint(str(fg_offset + x), str(bg_offset + x), "#")
		print("")
