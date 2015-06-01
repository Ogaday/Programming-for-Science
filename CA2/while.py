n = 0
while n<10:
	n += 1
	print n
	
n %= 13
print n

def deck(N = 52):
	deck = range(N)
	for n in deck:
		deck[n] %=13
		deck[n] += 1
	return deck

deck = deck()

deck = tuple(deck)
print deck

t = (1, 2, 3)

a, b, c = t
print a,
print b,
print c,
print len(t)



print '################################### \n'

def jqk(visible):
	"""
	return a tuple of the indices of the cards which form a set of jack quen and king.
	
	keyword arguemnts:
	visible -- the top cards in the piles.
	"""
	jqk = []
	n = 0
	while n < len(visible) and len(jqk) < 3:
		if visible[n] > 9:
			jqk.append(n)
		n += 1
	if len(jqk) != 3:											#might not be necessary anymore. function will only run if 11, 12, and 13 are in view.
		jqk = []
	jqk = tuple(jqk)
	return jqk

def jqk2(visible):												
	"""
	return a tuple of the indices of the cards which form a set of jack quen and king.
	
	keyword arguemnts:
	visible -- the top cards in the piles.
	"""
	jqk = [0, 0, 0]
	if 11 in visible and 12 in visible and 13 in visible:	#brief says function should check. I think it's easier to check outside the function...
		for i in range(len(visible)):
			if visible[i] == 11:
				jqk[0] = i
			elif visible[i] == 12:
				jqk[1] = i
			elif visible[i] == 13:
				jqk[2] = i
		jqk = tuple(jqk)
		return jqk
	
list = [3, 9, 11, 10, 12, 15, 13]
print jqk(list)
other = [0, 1, 2, 3]

print jqk2(list)






thingy = [0, 8, 21, 13, 3, 9, 10]
print thingy
elevens = []
for i in range(len(thingy)):
	for n in range(i+1, len(thingy)):
		if thingy[i] + thingy[n] == 11:
			elevens.append(i)
			elevens.append(n)
print elevens

def add_to_11(visible):
	"""
	return a tuple of the indices of the cards which add to eleven.
	
	keyword arguemnts:
	visible -- the top cards in the piles.
	"""
	elevens = [0, 0]
	for i in range(len(visible)):
		for n in range(i+1, len(visible)):
			if visible[i] + visible[n] == 11:
				elevens[0] = i
				elevens[1] = n
	if elevens == [0, 0]:
		return ()
	else:
		return tuple(elevens)

print add_to_11(thingy)


'''
	while len(deck) > 0 and len(visible) < 10:					
		if add_to_11(visible) != ():
			n = 0
			while len(deck)>0:
				for n in add_to_11(visible):
					visible[n] = deck[0]
					del deck[0]
				n+=1
		elif 11 in visible and 12 in visible and 13 in visible:
			n = 0
			while n < 3 and len(deck)>0:
			#for n in jqk(visible):								
				visible[jqk(visible)[n]] = deck[0]
				del deck[0]
				n += 1
'''
print [0]*53