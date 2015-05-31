def perfect(N):
	"""
	Sum the first N perfect squares
	"""
	L = range (1, N+1)  #iterable list of the first N natural numbers
	P = []				#list of squares of elements in L
	sumsq = 0			#sum of elements in L
	for i in range(len(L)):	
		P.append(L[i]**2)
		sumsq += P[i]
	return sumsq

sumsq = perfect(30)
print 'The sum of the first 30 perfect squares is ' +str(sumsq)