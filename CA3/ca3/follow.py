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
		elif s == "]":								#picks up t, and uses goto to make the most recently stored
			pu(t)									#coords and heading the current ones, and deletes them from 
			x = stack.pop(-1)						#the list. works from the back
			y = stack.pop(-1)
			heading = stack.pop(-1)
			goto(t, x, y, heading)
			pd(t)