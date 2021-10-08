from mathscii import *

iterations = 30
for density in range (1, iterations):
	c = getBlankCanvas(3, 80, 42)
	center = (int(len(c[0])/2), int(len(c)/2))
	iter = 0.0
	c_iter = 0
	for deg in range(360*density):
		c[int(center[1]+sin(deg)*(20/(iterations-density))*sin(iter))][int(center[0]+cos(deg)*(20/(iterations-density))*sin(iter))] = fg_range[int(c_iter)]-30
		iter += .01
		c_iter = 0 if c_iter >= 7 else c_iter+1
	printCanvas(c)
	time.sleep(.5)
	os.system("clear")
