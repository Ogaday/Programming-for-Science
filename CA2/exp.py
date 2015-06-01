from TurtleWorld import *

world = TurtleWorld()
world.delay = 0

bob = Turtle()
print bob

def square(t, length):
	for i in range(4):
		fd(t, length)
		rt(t, 90)

def polygon(t, n, length):
	"""
	draw a polygon with turtle "t", sides "n", and sidelength "length"
	"""
	
	angle = 180 - (180.0*(n-2.0)/n)
	colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'magenta']
	set_width(t, 10)
	for x in range(n):
		set_pen_color(t, colors[x%7])
		fd(t, length)
		lt(t, angle)

def spiral(D, theta, alpha, N):
	"""
	draw a spiral by iterating straight lines and turns
	
	keyword arguments:
	D -- the distance forward moved
	theta -- the angle turned at each iteration
	alpha -- the factor by which to increase D each iteration
	N -- the number of iterations
	"""
	
	for i in range(N):
		fd(bob, D*alpha**i)
		rt(bob, theta)
spiral(1, 2, 1.001, 1000)		
#square(bob, 100)
#square(bob, 250)
"""
pu(bob)
rt(bob, 90)
fd(bob, 300)
lt(bob, 90)
pd(bob)
"""
#for i in range(3, 30):
#	polygon(bob, i, 100)


wait_for_user()