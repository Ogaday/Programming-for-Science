#F -- move forward a fixed distance
#E -- move forwards by the same fixed distance as for F
#L -- turn left by a fixed angle;
#R -- turn right by a fixed angle
# All other symbold are ignored

from TurtleWorld import *

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
		elif s == "E":
			fd(t, step)
		elif s == "L":
			lt(t, angle)
		elif s == "R":
			rt(t, angle)
	wait_for_user()

			
if __name__ == "__main__":
	world = TurtleWorld()
	world.delay = 0
	bob = Turtle()
	follow(bob, "FRFLFRFLFRFLFRFLFFFLLFRFLFRFLFRFLFRFLFLLFRLFRFLF", 15, 45)


