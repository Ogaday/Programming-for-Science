from TurtleWorld import *
from random import random
from math import sqrt

def walk(n):
	"""
	generate and return a string of n characters randomly and evenly chosen from N, E, S, W
	"""
	walk = ""
	try:
		for i in range(n):
			direction = random()
			if direction < 1/3.0:
				walk += "F"
			elif direction < 2/3.0:
				walk += "L"
			else:
				walk += "R"

		return walk
	except:
		return "invalid argument passed"

def follow(t, S, step = 10, angle = 90):
	"""
	read a string and interpret the symbols as instructions
	
	keyword arguments:
	t -- turtle
	S -- string of instructions
	step -- distance moved each time
	angle -- angle turned each time
	"""
	
	for s in S:								#iterates through the string "S" and interprets the element apropriately, ie. if that element is "F", it moves forward.
		if s == "F":
			fd(t, step)
		elif s == "L":
			lt(t, angle)
			fd(t, step)
		elif s == "R":
			rt(t, angle)
			fd(t, step)
	wait_for_user()
	
def where(t):
	return (where_x(t), where_y(t))

def displacement(t):
	return sqrt(where_x(t)**2 + where_y(t)**2)


#############################################################################



def coord_finder(S):
	"""
	return the coord of a turtle/drunk after it follows the string S, without
	using swampy. Has to follow foward/left/right instructions, while measuring
	displacement with (x, y)...
	"""
	x = 0
	y = 0
	orientation = 0
	for s in S:
		if orientation == 0:
			if s == "F":
				x += 1
			elif s == "L":
				y += 1
				orientation = 1
			elif s == "R":
				y -= 1
				orientation = 3
		elif orientation == 1:
			if s == "F":
				y += 1
			elif s == "L":
				x -= 1
				orientation = 2
			elif s == "R":
				x += 1
				orientation = 0
		elif orientation == 2:
			if s == "F":
				x -= 1
			elif s == "L":
				y -= 1
				orientation = 3
			elif s == "R":
				y += 1
				orientation = 1
		elif orientation == 3:
			if s == "F":
				y -= 1
			elif s == "L":
				x += 1
				orentation = 0
			elif s == "R":
				x -= 1
				orientation = 2
	return (x, y)

def displacement_2(S):
	x, y = coord_finder(S)
	return sqrt(x**2 + y**2)
	
	
world = TurtleWorld ()
t = Turtle ()
world.delay = 0

drunken_wander = walk(75)
print drunken_wander
print "drunk ended up at coords ", coord_finder(drunken_wander)
print "drunk has a displacement of ", displacement_2(drunken_wander)
follow(t, drunken_wander, 1)
print "drunk ended up at coords ", where(t)
print "drunk has a displacement of ", displacement(t)

