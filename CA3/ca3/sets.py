def legalize(L):
	"""
	keyword arguments:
	L -- a list
	
	returns:
	legal -- the list Lin the form of a legal set, ie. no repeated elements
	"""
	legal = []
	for i in L:							#for each item in L, appends it to legal if it is not already in legal
		if not i in legal:
			legal.append(i)
	return legal

def union(A, B):
	"""
	return the legal union of two sets
	"""
	return legalize(A+B)				#uses list addition, then legalises the result

def intersection(A, B):
	"""
	return the legal intersect of two sets
	"""
	return filter(lambda x: x in B, A)	#for each of the elements of A, if they are in B, return them as a list

def remove(A, e):
	"""
	removes each element "e" in the list/set A
	"""
	while e in A:				#while means it is protected from removing elements which are not members of the set A, and multiples of elements
		del A[A.index(e)]		#or remove A[e]
	return A
	
def difference(A, B):
	"""
	return the set set difference of A and B (A\B)
	"""
	return filter(lambda x: not x in B, A)		#return each element in A, if it is not a member of B

def test(A, B, e):
	"""
	tests the functions union, intersection, remove and fifference using the sets A, B and the element e
	"""
	print "union of", A, "and", B, ":", union(A, B)
	print "intersection of", A, "and", B, ";", intersection(A, B)
	print "removal of", e, "from", A, ":", remove(A, e)
	print "set difference of", A, "and", B, ":", difference(A, B)

def F(e, T):
	"""
	function used to recursively create a powerset.
	
	adds e to each set in T
	"""
	return [x+[e] for x in T]
	
def powerset(S):
	"""
	recursivley finds the powerset of S according to the algorithm almost exactly
	"""
	if S == []:
		return [[]]
	else:
		e = S[0]
		T = difference(S, [e])
		return union(powerset(T), F(e, powerset(T)))
		
if __name__ == "__main__":
	A = [1,2,3,4]
	B = [1,2,2,3]
	C = [5]
	D = []
	print A, legalize(A)
	print B, legalize(B)
	print C, legalize(C)
	print D, legalize(D)
	
	test([1,2,3,4], [3,4,5,6], 2)
	
	greek = ["alpha", "beta", "gamma", "delta", "epsilon"]
	print greek, powerset(greek)
	
	
	