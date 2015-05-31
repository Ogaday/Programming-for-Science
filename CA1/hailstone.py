def hailstone(n):
	"""
	append the terms of a hailstone sequence to the list sequence.
	return sequence
	"""
	sequence = []

	def path(n):
		"""
		generate a term in a hailstone sequence
		"""
		sequence.append(n)
		if n == 1:
			return n
		elif n%2 == 0:
			n = n/2
			return path(n)
		else:
			n = 3*n + 1
			return path(n)
	
	path(n)
	return sequence


print 'The first ten sequences of hailstone numbers are:'	#prints the first 10 hailstone sequences
for number in range (1, 11):
	H = hailstone(number)
	print H


lengths = []
for i in range (3, 10001): 		#finds the lengths of sequences starting with numbers 3 to 1000 and appends them to a list
	H = hailstone(i)
	lengths.append(len(H))

max = lengths[0]
min = lengths[0]
sum = 0.0
for i in range(len(lengths)): 	#finds the longest sequence, shortest sequence, and sum of sequences for average later
	if lengths[i] > max:
		max = lengths[i]
	if lengths[i] < min:
		min = lengths[i]
	sum += lengths[i]


for i in range (3, 10000):		#finds the starting terms of the longest and shortest sequences
	if len(hailstone(i)) == max:
		a = hailstone(i)[0]
	if len(hailstone(i)) == min:
		b = hailstone(i)[0]

avg = sum/len(lengths)

print 'Between starting points of 3 and 10000, the shortest sequence starts with', b, ' and is ', min, ' terms long. The longest sequence starts with', a, 'and is ', max, 'terms long, and the average sequence length is ', avg