from TurtleWorld import *
from follow2 import follow


def sierpinski_print(S, n):
	if n == 0:
		print S,
	else:
		for s in S:
			if s == "E":
				sierpinski_print("FLELF", n-1)
			elif s == "F":
				sierpinski_print("ERFRE", n-1)
			else:
				print s,

def sierpinski_write(axiom):
	S = ""
	for a in axiom:
		if a == "E":
			S += "FLELF"
		elif a == "F":
			S += "ERFRE"
		else:
			S+= a
	return S
	
def sierpinski(S, n, t, step = 2, angle =60):
	for i in range(n):
		 S = sierpinski_write(S)
	follow(bob, S, step = 2, angle = 60)
	
if __name__ == "__main__":
	sierpinski_print("E", 2)
	world = TurtleWorld()
	world.delay = 0
	bob = Turtle()
	#follow(bob, "FLELFRERFRERFLELFLERFRELFLELFLERFRELFLELFRERFRERFLELFRERFRELFLELFLERFRERFLELFRERFRERFLELFRERFRELFLELFLERFRERFLELFRERFRERFLELFLERFRELFLELFLERFRELFLELFRERFRRFLELFLERFRELFLELFLERFRERFLELFRERFRERFLELFRERFRELFLELFLERFRELFLELFRERFRERFLELFLERFRELFLELFLERFRELFLELFRERFRERFLELFLERFRELFLELFLERFRERFLELFRERFRERFLELFRERFRELFLELFLERFRELFLELFRERFRERFLELFLERFRELFLELFLERFRELFLELFRERFRERFLELFRERFRELFLELFLERFRERFLELFRERFRERFLELFRERFRELFLELFLERFRERFLELFRERFRERFLELFLERFRELFLELFLERFRELFLELFRERFRERFLELF", 2, 60)
	sierpinski("E", 12, bob, step = 2, angle = 60)
	
	#wait_for_user()
		