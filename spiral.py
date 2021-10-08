from mathscii import *
from math import sin
from math import cos
os.system("clear")
w, h = 150, 40
c = getBlankCanvas(3, w, h)
size = 1
color = 1
for deg in range(360*5):
	size += .01
	try:
		c[int(h/2)+int(cos(deg/10)*size)][int(w/2)+int(sin(deg/10)*size)] = color
	except: pass
	color = color+1 if color <= 6 else 1
printCanvas(c)
