from TurtleWorld import *

def sierpinski_print(S, n):
	"""
	recursively writes the nth rewriting of the axiom S according to the sierpinski rewriting rules
	
	keyword arguments:
	S -- the axiom for the rewrite. must be a single character string
	n -- the number of rewrites, and the depth of conversion
	
	rules:
	axiom = "E"
	"E" --> "FLELF"
	"F" --> "ERFRE"
	All other characters remain unchanged
	"""
	if n == 0:								#base case
		return S
	if S == "E":							#recursive case
		S = ''.join([sierpinski_print(x, n-1) for x in "FLELF"])	#rewrites each element in the 
	elif S == "F":							#recursive case			#rewritten case, so the function 
		S = ''.join([sierpinski_print(x, n-1) for x in "ERFRE"])	#only takes 1 character atr a time
	return S

def follow(t, S, step=10, angle=90):
	"""
	turtle t follows the instructions in the string S, using a step and angle
	
	following rules:
	E -- step forward "step" units
	F -- step forward "step" units
	L -- turn left "angle" degrees
	R -- turn right "angle" degrees
	All other characters disregard
	"""
	for s in S:
		if s == 'E':
			fd(t, step)
		elif s == 'F':
			fd(t, step)
		elif s == 'L':
			lt(t, angle)
		elif s == 'R':
			rt(t, angle)

def sierpinski(S, n, t, step = 2, angle =60):
	S = sierpinski_print(S, n)
	follow(bob, S, step = 2, angle = 60)

if __name__ == "__main__":
	#print sierpinski_print("E", 2)
	world = TurtleWorld()
	world.delay = 0
	bob = Turtle()
	pu(bob)
	lt(bob)
	fd(bob, 300)
	rt(bob)
	pd(bob)
	sierpinski("E", 10, bob)
	wait_for_user()