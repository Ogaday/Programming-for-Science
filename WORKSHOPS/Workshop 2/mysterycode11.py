#look out for the inifite loop! Hit ctrl - C to stop.
L = [1]
for x in L:
	print L
	L.append(x+1)