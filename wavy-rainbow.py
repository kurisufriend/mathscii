from mathscii import *
c = getBlankCanvas(3, 70, 30)

"""
for y in range(0, len(c)):
	for x in range(0, len(c[0])):
		try:
			c[int(sin(x/10)*10 + y)][x] = int(y/30 * 8)
		except:
			pass
"""
for spin in range(-50, 50):
	for y in range(0, len(c)):
		for x in range(0, len(c[0])):
			try:
				c[x][int(sin(x/10)*spin + y)] = int(y/30 * 8)
			except:
				pass
#		print("\n"*100)
#		os.system("clear")
		printCanvas(c)
		time.sleep(.2)
