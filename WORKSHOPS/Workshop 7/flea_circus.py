from random import random

def circus(n, steps):
	"""
	in an nxn grid, each square is occupied initially by a single flea, which jumps
	at random in one of four directions, by analogy N, E, S or W. return the number
	of unnocupied squares after this mad exercise
	
	keyword arguments:
	
	n -- the dimensions of the imaginarium
	steps -- how many iterations the pandemonium runs through
	
	keywords:
	
	menagerie -- let each flea be defined non uniquely by it's temporal and
	spatial properties (ironically, only 3 dimensions in this case, on an
	axis of x and y, and at step in time)
	imaginarium -- imagine...imagine...imagine a story! an interpretive dance in 1-d space and
	decimal integers of how many fleas rest where after jumping steps
	"""
	
	menagerie = []									#the first keyword appears, and aptly, there are
													#as many fleas as squares in the menagerie
	for i in range(n**2):
		menagerie.append([i%n, i/n])
		
	for s in range(steps):
		for flea in menagerie:
			jump = random()
			if jump < 0.25:
				flea[0] += 1
			elif jump <0.5:
				flea[1] += 1
			elif jump <0.75:
				flea[0] -= 1
			else:
				flea[1] -= 1
			for i in range(len(flea)):								#decision time...do fleas bounce, stay, wrap around, or 
				if flea[i] > (n-1):								#snakes and ladder(probably not the latter)? I actually
					flea[i] = (n-1)								#like wrapping...
				if flea[i] < 0:									#am using sticking, though because I think that that is the best bet.
					flea[i] = 0
	
	imaginarium = [0]*n**2
	
	for flea in menagerie:
		imaginarium[flea[1]*n+flea[0]] +=  1
	return imaginarium								#list of how many fleas according to linear location in a list

def unoccupied(n, steps):						#might make the circus fucntion output the other function inputs.
	"""
	after n steps, count the whitespaces!
	"""
	positions = circus(n, steps)
	empties = 0
	for i in positions:
		if i == 0:
			empties += 1
	return empties

def average_unoccupied(n, steps, many):
	"""
	if you were to go to the flea circus many times, you would undoubtedly count
	which positions were empty, and collate the results in an
	avergae day at the circus
	"""
	sum = 0
	for i in range(many):
		empties = unoccupied(n, steps)
		sum += empties
	return sum/many
	
def visualise(n, steps):
	"""
	bring to life the speculiar incidence of the n**2 jumping fleas upon a matrix of n rows and n columns!
	"""
	imaginarium = circus(n, steps)
	cage = []
	for i in range(n):
		cage += [imaginarium[i*n:i*n+n]]
	return cage
	
cage = visualise(30, 50)
for n in cage:
	print n