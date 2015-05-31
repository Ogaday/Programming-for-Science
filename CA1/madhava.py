def madhava(N):
	"""
	Define the first N terms of Madhava's sequence, and the sum of the first N terms.
	"""
	
	Terms = []			#first N terms of Madhava's sequence
	sum = 0.0			#sum of the first N terms
	Partialsums = []	#cumulative sums of the first N terms
	from math import sqrt
	
	for n in range(N):
		u = sqrt(12.0)*(-3.0)**(-n)/(2.0*n+1.0)	#expression for the Nth term
		Terms.append(u)
		sum += u 								#Madhhava's nth approximation of pi
		Partialsums.append(sum)
	
	return Partialsums


PS	=  madhava(20)
print 'The first 20 partial sums from Madhava\'s sequence are:'
print PS, '\n'
from math import pi

for i in range(0, 20):
	print 'The difference from pi in term '+ str(i+1) + ' is ', abs(PS[i] - pi)

i = 0
while abs(PS[i] - pi) > (0.000001):
	i+=1

print 'Accuracy is better than 1 part in a million at the ' +str(i+1) + 'th term: ', PS[i]
