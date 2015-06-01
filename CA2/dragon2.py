from TurtleWorld import *
from follow import follow

def dragon(S):
	"""
	rewrite the string "S" according to Heighway dragon SRS
	
	Axiom -- FA
	
	Rules:
	A --> ARBF
	B --> FALB
	All of the other characters remain unchanged
	"""
	stage_1 = ""
	for s in S:
		if s == "A":
			stage_1 += "ARBF"
		elif s == "B":
			stage_1 += "FALB"
		else:
			stage_1 += s
	return stage_1

			

if __name__ == "__main__":
	world = TurtleWorld()
	world.delay = 0
	bob = Turtle()
	
	pu(bob)
	fd(bob, 700)
	rt(bob)
	fd(bob, 300)
	lt(bob)
	pd(bob)
	axiom = "FAAAAAAAAAFAB"
	for i in range(12):
		axiom = dragon(axiom)
	follow(bob, axiom, 3, 90)
	wait_for_user()