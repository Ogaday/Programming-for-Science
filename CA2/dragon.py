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
	if type(S) != str:
		return "invalid argument type"
	
	stage_1 = ""								#creates a new string, and concatenates the rewritten string to it
	for s in S:
		if s == "A":
			stage_1 += "ARBF"					#A --> ARBF
		elif s == "B":
			stage_1 += "FALB"					#B --> FALB
		else:
			stage_1 += s						#No other elements are changed
	return stage_1

			

if __name__ == "__main__":
	world = TurtleWorld()
	world.delay = 0
	bob = Turtle()

	axiom = "FA"
	for i in range(12):
		axiom = dragon(axiom)
	pu(bob)
	fd(bob, 200)
	pd(bob)
	follow(bob, axiom, 5, 90)