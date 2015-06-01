def circumcircle(a, b, c):
	"""
	return the radius of the circumcircle which passes through the vertices of a triangle with sides of length a, b and c if no two side lengths sum to be less than the third, in which case return None and an error message.
	"""
	#test for error conditions
	if a + b < c or a + c < b or b + c < a:
		print 'Invalid triagle!'
	else:
		#fine semiperimeter
		s = (a + b + c)/2.0
	
		#find diamter
		d = (a*b*c)/(2.0*(s*(s-a)*(s-b)*(s-c))**0.5)
	
		#find radius: r
		r = d/2
	
		return r

print circumcircle(3, 7.9, 5)
def test_circumcircle():
	
	#test for accuracy in known case
	test1 = circumcircle(3, 4, 5) == 2.5
	
	#test for false cases
	test2 = circumcircle(1, 1, 3) == None
	return (test1, test2)

#a, b = test_circumcircle()
#print a, b