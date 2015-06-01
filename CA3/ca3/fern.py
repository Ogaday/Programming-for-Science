from TurtleWorld import *

def fern_write(S, n):
	"""
	recursively writes the nth rewriting of the axiom S according to the fern rewriting rules
	
	keyword arguments:
	S -- the axiom for the rewrite. must be a single character string
	n -- the number of rewrites, and the depth of conversion
	
	rules:
	axiom = "A"
	"A" --> "FL[[A]RA]RF[RFA]LA"
	"F" --> "FF"
	All other characters remain unchanged
	"""
	if n == 0:
		return S
	if S == "A":
		S = ''.join([fern_write(x, n-1) for x in "FL[[A]RA]RF[RFA]LA"])
	elif S == "F":
		S = ''.join([fern_write(x, n-1) for x in "FF"])
	return S

def follow(t, S, stack, step=10, angle=90):
	"""
	turtle t follows the instructions in the string S, using a step and angle
	
	following rules:
	E -- step forward "step" units
	F -- step forward "step" units
	L -- turn left "angle" degrees
	R -- turn right "angle" degrees
	[ -- stores the current x coord, y coord, and heading in a stack
	] -- retrieves most recent x coord, y coord, and heading from stack, and
		makes that the turtle t's current position
	All other characters disregard
	"""
	#The color is just a bit of fun. Everytime a location is saved, the turtle's
	#path changes color, and it cycles through the available colors indefinitely.
	#uncomment lines 43, 57, 58, 72 for the display
	
	#n = 0
	for s in S:
		if s == "E" or s == "F":
			fd(t, step)
		elif s == "L":
			lt(t, angle)
		elif s == "R":
			rt(t, angle)
		elif s == "[":								#stores current location and heading in stack
			x, y = where(t)
			heading = get_heading(t)
			stack.append(heading)
			stack.append(y)
			stack.append(x)	
			#set_pen_color(t, colors[(n)%len(colors)])
			#n += 1
		elif s == "]":								#picks up t, and uses goto to make the most recently stored
			pu(t)									#coords and heading the current ones, and deletes them from 
			x = stack.pop(-1)						#the list. works from the back
			y = stack.pop(-1)
			heading = stack.pop(-1)
			goto(t, x, y, heading)
			pd(t)

def fern(S, n, t, stack=[], step=4, angle=25):
	S = fern_write(S, n)
	follow(t, S, stack, step, angle)

if __name__ == "__main__":
	#colors = ['red', 'orange', 'green', 'blue', 'violet', 'magenta']
	world = TurtleWorld()
	bob = Turtle()
	world.delay = 0.01
	pu(bob)
	rt(bob)
	fd(bob, 300)
	lt(bob)
	lt(bob)
	pd(bob)
	fern("A", 6, bob, stack = [], step = 7, angle = 25)
	wait_for_user()