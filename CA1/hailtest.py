#don't touch anything below this line!
sequence = []
def hailstone(n):
	P = path(n)
	return sequence

def path(n):
	sequence.append(n)
	if n == 1:
		return n
	elif n%2 == 0:
		n = n/2
		return path(n)
	else:
		n = 3*n + 1
		return path(n)
#Don't touch anything above this line!

print 'the first ten sequences of hailstone numbers are:'
for number in range (1, 11):
	H = hailstone(number)
	print H

	
lengths = []
for number in range (3, 10000):
	H = hailstone(number)
	lengths.append(len(H))

max = lengths[0]
min = lengths[0]
sum = 0.0
for length in lengths:
	if length > max:
		max = length
	if length < min:
		min = length
	sum += length

avg = sum/len(lengths)

print 'Between starting points of 3 and 10000, min sequence length is', min, ', max sequence length is', max, ', and average sequence length is ', avg