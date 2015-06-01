from TurtleWorld import *

#def sierpinski_print(S, n):
#	if n == 0:
#		return S
#	for i in range(len(S)):
#		if S[i] == "E":
#			del S[i]
#			S.insert(i, sierpinski_print("FLELF", n-1))
#		elif S[i] == "F":
#			S[i] = sierpinski_print("ERFRE", n-1)
#		else:
#			S[i] = sierpinski_print([S[i]], n-1)
#	return S

	
#def sierpinski_print(S, n):
##	if n == 0:
##		return ''.join(S)
##	for i in range(len(S)):
##		if S[i] == "E":
##			del S[i]
##			for l in "FLELF":
##				S.insert(i, sierpinski_print([l], n-1))
##		elif S[i] == "F":
##			del S[i]
##			for l in "ERFRE":
##				S.insert(i, sierpinski_print([l], n-1))
##		else:
##			S[i] = sierpinski_print(S[i], n-1)
##	return S

def sierpinski_print(S, n):
	if n == 0:
		return S
	if S == "E":
		S = ''.join([sierpinski_print(x, n-1) for x in "FLELF"])
	elif S == "F":
		S = ''.join([sierpinski_print(x, n-1) for x in "ERFRE"])
#	else:
#		S = sierpinski_print(S, n-1)
	return S

def follow(t, S, step=10, angle=90):
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
	print sierpinski_print("E", 2)
	world = TurtleWorld()
	world.delay = 0
	bob = Turtle()
	sierpinski("E", 8, bob)
	wait_for_user()