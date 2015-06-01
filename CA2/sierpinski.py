from follow import follow
from TurtleWorld import *


def sierpinski(S):
	"""
	rewrite the string "S" according to the SRS:
	
	Symbols - EFLR
	
	Axiom -- E
	
	Rules:
	E -->FLELF
	F --> ERFRE
	All of the other characters remain unchanged
	"""
	if type(axiom) != str:
		return "invalid argument type"
	
	stage_1 = ""
	for s in S:
		if s == "E":
			stage_1 += "FLELF"		#E -->FLELF
		elif s == "F":
			stage_1 += "ERFRE"		#F --> ERFRE
		else:
			stage_1 += s			#All of the other characters remain unchanged
	return stage_1
	
if __name__ == "__main__":
	world = TurtleWorld()
	world.delay = 0
	bob = Turtle()
	axiom = "E"
	for n in range(8):
		axiom = sierpinski(axiom)
	pu(bob)
	lt(bob)
	fd(bob, 200)
	lt(bob)
	fd(bob, 200)
	lt(bob)
	lt(bob)
	pd(bob)
	
	follow(bob, axiom, 2, 60)