from TurtleWorld import *
from follow2 import follow
X = ""	
def sierpinski_print(S, n):
	if n == 0:
		X += S
	else:
		for s in S:
			if s == "E":
				sierpinski_print("FLELF", n-1)
			elif s == "F":
				sierpinski_print("ERFRE", n-1)
			else:
				X += s

			
sierpinski_print("E", 3)
print X
				

def sierpinski(S, n, t, step = 2, angle =60):
	X = ""
	S = sierpinski_print(S, n, X)
	follow(bob, S, step = 2, angle = 60)
	
	