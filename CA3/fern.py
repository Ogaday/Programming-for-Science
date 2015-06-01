from TurtleWorld import *
from follow2 import follow

def fern_write(axiom):							#NEEDS REWRITING D:
	S = ""
	for a in axiom:
		if a == "A":
			S += "FL[[A]RA]RF[RFA]LA"
		elif a == "F":
			S += "FF"
		else:
			S += a
	return S

def follow(t, S, stack, step=10, angle=90):
	n = 0
	for s in S:
		if s == "E" or s == "F":
			fd(t, step)
		elif s == "L":
			lt(t, angle)
		elif s == "R":
			rt(t, angle)
		elif s == "[":
			x, y = where(t)
			heading = get_heading(t)
			stack.append(heading)
			stack.append(y)
			stack.append(x)	
			set_pen_color(t, colors[(n)%len(colors)])
			n += 1
		elif s == "]":
			pu(t)
			x = stack.pop(-1)
			y = stack.pop(-1)
			heading = stack.pop(-1)
			goto(t, x, y, heading)
			pd(t)

def fern(S, n, t, stack=[], step=4, angle=25):				#NEEDS REWRITING RECURSIVELY? 	base case: follow S, else: fern recurse? fuckfuckfuckittyfuck
	for i in range(n):
		S = fern_write(S)
	follow(t, S, stack, step, angle)

colors = ['red', 'orange', 'green', 'blue', 'violet', 'magenta']

if __name__ == "__main__":
	world = TurtleWorld()
	bob = Turtle()
	world.delay = 0
	pu(bob)
	rt(bob)
	fd(bob, 300)
	lt(bob)
	lt(bob)
	pd(bob)
	A = "A"
	for i in range(2):
		A =  fern_write(A)
	print A
	#fern("A", 6, bob, stack = [], step = 4, angle = 25)
	wait_for_user()